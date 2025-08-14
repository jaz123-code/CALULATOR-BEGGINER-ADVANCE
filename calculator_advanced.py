#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator GUI with History
---------------------------
A simple Tkinter calculator that:
- Evaluates arithmetic expressions (+, -, *, /, %, **, parentheses, decimals).
- Saves each successful calculation to a history file.
- Shows history in a side panel; click an item to reuse it.
- Lets you clear history or delete the selected history entry.
- Provides keyboard input (numbers, operators, Enter for =, Backspace, Escape for Clear).

Files:
- History file defaults to "history.txt" in the same folder as this script.
"""

import ast
import operator
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path

# ---------- Configuration ----------
HISTORY_FILE = Path(__file__).with_name("history.txt")

# ---------- Safe Evaluator ----------
_ALLOWED_BINOPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
_ALLOWED_UNARYOPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

def _eval_node(node):
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only numbers are allowed.")
    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_BINOPS:
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        return _ALLOWED_BINOPS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_UNARYOPS:
        operand = _eval_node(node.operand)
        return _ALLOWED_UNARYOPS[type(node.op)](operand)
    if isinstance(node, ast.Expr):
        return _eval_node(node.value)
    raise ValueError(f"Unsupported expression element: {type(node).__name__}")

def safe_eval(expr: str):
    try:
        parsed = ast.parse(expr, mode="eval")
        return _eval_node(parsed.body)
    except ZeroDivisionError:
        raise
    except Exception as e:
        raise ValueError(str(e))

# ---------- History Helpers ----------
def read_history():
    if not HISTORY_FILE.exists():
        return []
    try:
        lines = HISTORY_FILE.read_text(encoding="utf-8").splitlines()
        return [ln for ln in lines if ln.strip()]
    except Exception:
        return []

def append_history(expression, result):
    line = f"{expression} = {result}"
    try:
        with HISTORY_FILE.open("a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception as e:
        print(f"Could not write history: {e}")

def write_history(lines):
    try:
        with HISTORY_FILE.open("w", encoding="utf-8") as f:
            f.write("\n".join(lines) + ("\n" if lines else ""))
    except Exception as e:
        print(f"Could not write history: {e}")

# ---------- GUI ----------
class CalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator with History")
        self.geometry("520x480")
        self.minsize(520, 420)

        # Top frame: entry + buttons
        top = ttk.Frame(self, padding=8)
        top.pack(fill="x")

        self.expr_var = tk.StringVar()
        self.entry = ttk.Entry(top, textvariable=self.expr_var, font=("Arial", 18))
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 8))
        self.entry.focus_set()

        self.eq_btn = ttk.Button(top, text="=", width=4, command=self.evaluate)
        self.eq_btn.pack(side="left")
        self.clear_btn = ttk.Button(top, text="C", width=4, command=self.clear_entry)
        self.clear_btn.pack(side="left", padx=(8, 0))

        # Main split: keypad and history
        main = ttk.Frame(self, padding=8)
        main.pack(fill="both", expand=True)

        # Keypad
        keypad = ttk.Frame(main)
        keypad.pack(side="left", fill="both", expand=True, padx=(0, 8))

        buttons = [
            ("7",), ("8",), ("9",), ("/",),
            ("4",), ("5",), ("6",), ("*",),
            ("1",), ("2",), ("3",), ("-",),
            ("0",), (".",), ("(",), (")",),
            ("%",), ("//",), ("**",), ("+",),
        ]

        rows, cols = 5, 4
        for i in range(rows):
            keypad.rowconfigure(i, weight=1)
        for j in range(cols):
            keypad.columnconfigure(j, weight=1)

        idx = 0
        for r in range(rows):
            for c in range(cols):
                if idx >= len(buttons):
                    break
                label = buttons[idx][0]
                ttk.Button(keypad, text=label, command=lambda t=label: self.insert_text(t)).grid(row=r, column=c, sticky="nsew", padx=4, pady=4)
                idx += 1

        backspace = ttk.Button(keypad, text="⌫", command=self.backspace)
        backspace.grid(row=rows, column=0, columnspan=2, sticky="nsew", padx=4, pady=4)
        clr = ttk.Button(keypad, text="Clear", command=self.clear_entry)
        clr.grid(row=rows, column=2, sticky="nsew", padx=4, pady=4)
        evalb = ttk.Button(keypad, text="Evaluate", command=self.evaluate)
        evalb.grid(row=rows, column=3, sticky="nsew", padx=4, pady=4)

        # History panel
        right = ttk.Frame(main)
        right.pack(side="left", fill="both")

        title_row = ttk.Frame(right)
        title_row.pack(fill="x")
        ttk.Label(title_row, text=f"History ({HISTORY_FILE.name})", font=("Arial", 12, "bold")).pack(side="left")
        ttk.Button(title_row, text="Clear All", command=self.clear_history).pack(side="right")

        self.history = tk.Listbox(right, activestyle="dotbox")
        self.history.pack(fill="both", expand=True, pady=6)

        btn_row = ttk.Frame(right)
        btn_row.pack(fill="x")
        ttk.Button(btn_row, text="Use", command=self.use_selected).pack(side="left")
        ttk.Button(btn_row, text="Delete", command=self.delete_selected).pack(side="left", padx=6)
        ttk.Button(btn_row, text="Refresh", command=self.refresh_history).pack(side="left")

        # Status bar
        self.status = tk.StringVar(value="Ready")
        ttk.Label(self, textvariable=self.status, anchor="w").pack(fill="x", padx=8, pady=(0,6))

        # Keyboard bindings
        self.bind("<Return>", lambda e: self.evaluate())
        self.bind("<KP_Enter>", lambda e: self.evaluate())
        self.bind("<Escape>", lambda e: self.clear_entry())
        self.bind("<BackSpace>", lambda e: self.backspace())

        self.refresh_history()

    # ----- UI helpers -----
    def insert_text(self, text):
        self.entry.insert("insert", text)

    def backspace(self):
        pos = self.entry.index("insert")
        if pos > 0:
            self.entry.delete(pos-1)

    def clear_entry(self):
        self.expr_var.set("")
        self.status.set("Cleared")

    # ----- History actions -----
    def refresh_history(self):
        self.history.delete(0, "end")
        for line in read_history():
            self.history.insert("end", line)

    def clear_history(self):
        if messagebox.askyesno("Clear History", "Delete all history entries?"):
            write_history([])
            self.refresh_history()

    def delete_selected(self):
        i = self.history.curselection()
        if not i:
            return
        idx = i[0]
        lines = read_history()
        if 0 <= idx < len(lines):
            del lines[idx]
            write_history(lines)
            self.refresh_history()

    def use_selected(self):
        i = self.history.curselection()
        if not i:
            return
        text = self.history.get(i[0])
        if " = " in text:
            expr = text.split(" = ", 1)[0]
        else:
            expr = text
        self.expr_var.set(expr)
        self.entry.icursor("end")
        self.status.set("Loaded from history")

    # ----- Evaluation -----
    def evaluate(self):
        expr = self.expr_var.get().strip()
        if not expr:
            return
        try:
            result = safe_eval(expr)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            append_history(expr, result)
            self.refresh_history()
            self.expr_var.set(str(result))
            self.entry.icursor("end")
            self.status.set(f"OK: {expr} = {result}")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero")
            self.status.set("Error: Division by zero")
        except Exception as e:
            messagebox.showerror("Invalid Expression", str(e))
            self.status.set(f"Error: {e}")

def main():
    app = CalculatorGUI()
    app.mainloop()

if __name__ == "__main__":
    main()
