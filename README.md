# CALULATOR-BEGGINER-ADVANCE
Its a calculators made my jaz , In this project I have created both beginner and advance level calculator with gui
# 🧮 Calculator Project

> **A comprehensive educational calculator project with both CLI and GUI implementations**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 📖 Project Overview and Goals

The **Calculator Project** is a comprehensive educational tool designed to demonstrate Python programming concepts through two distinct calculator implementations. This project serves multiple learning objectives:

### 🎯 Primary Goals
- **Educational Focus**: Provide clear, well-documented examples for Python learners at different skill levels
- **Progressive Learning**: Start with simple CLI concepts and advance to complex GUI programming
- **Best Practices**: Demonstrate proper code organization, testing, documentation, and version control
- **Real-World Applications**: Show how to build practical tools with Python's standard library

### 🌟 Key Learning Outcomes
- Command-line interface development
- GUI programming with Tkinter
- File I/O operations and data persistence
- Error handling and input validation
- Code organization and modular design
- Testing and documentation practices

---

## ⚡ Quick Start (TL;DR)

**Get up and running in 30 seconds:**

```bash
# Clone and setup
git clone https://github.com/yourusername/calculator-project.git
cd calculator-project
pip install -r requirements.txt

# Run CLI version
python beginner-cli/calculator_beginner.py

# Run GUI version
python advanced-gui/calculator_advanced.py
```

**That's it!** No complex setup, no external databases, just pure Python.

---

## 🔄 Feature Matrix (CLI vs GUI)

| Feature | CLI Version | GUI Version | Notes |
|---------|-------------|-------------|-------|
| **Basic Arithmetic** | ✅ | ✅ | +, -, *, /, %, ** |
| **Parentheses Support** | ✅ | ✅ | Complex expressions |
| **Decimal Numbers** | ✅ | ✅ | Float precision |
| **History Management** | ✅ | ✅ | Persistent across sessions |
| **Error Handling** | ✅ | ✅ | Safe evaluation |
| **Interactive Interface** | Terminal Menu | Button Grid | Different UX approaches |
| **Visual Feedback** | Text Output | Status Bar | User experience |
| **History Viewing** | List Display | Clickable List | Reusable entries |
| **History Export** | ❌ | ✅ | File operations |
| **Keyboard Shortcuts** | ❌ | ✅ | Enter, Escape, Backspace |
| **Visual Themes** | ❌ | ✅ | GUI styling |
| **Advanced Math** | ❌ | 🔄 | Floor division, modulo |
| **Memory Functions** | ❌ | 🚧 | Planned feature |
| **Scientific Functions** | ❌ | 🚧 | Planned feature |

**Legend:** ✅ Implemented | ❌ Not Available | 🔄 Basic Implementation | 🚧 Planned

---

## 💾 Installation

### Option 1: PyPI Installation (Recommended for Users)

```bash
# Install from PyPI (when published)
pip install calculator-project

# Run directly
calculator-cli    # CLI version
calculator-gui    # GUI version
```

### Option 2: Clone Repository (Recommended for Developers)

```bash
# Clone the repository
git clone https://github.com/yourusername/calculator-project.git
cd calculator-project

# Create virtual environment (recommended)
python -m venv calculator-env
source calculator-env/bin/activate  # On Windows: calculator-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Optional: Install in development mode
pip install -e .
```

### System Requirements
- **Python**: 3.8 or higher
- **OS**: Windows, macOS, Linux
- **Dependencies**: numpy, scipy (for advanced features)
- **GUI**: Tkinter (included with Python)

---

## 🚀 Usage

### CLI Calculator Usage

**Interactive Menu Mode:**
```bash
# Direct execution
python beginner-cli/calculator_beginner.py

# As a module
python -m beginner_cli.calculator_beginner
```

**Sample CLI Session:**
```
Welcome to the calculator with history feature!
1. CALCULATE  2. SHOW HISTORY  3. CLEAR HISTORY  4. EXIT
Enter your choice: 1
Enter the equation to calculate: 15 * 8 + 12
Result: 132
Result saved to history

1. CALCULATE  2. SHOW HISTORY  3. CLEAR HISTORY  4. EXIT
Enter your choice: 2
15 * 8 + 12 = 132
```

**Programmatic Usage:**
```python
from beginner_cli.calculator_beginner import calculate, show_history

# Direct calculation
result = calculate("25 + 17")
print(f"Result: {result}")

# Show calculation history
show_history()
```

### GUI Calculator Usage

**Launch GUI Application:**
```bash
# Direct execution
python advanced-gui/calculator_advanced.py

# As a module
python -m advanced_gui.calculator_advanced
```

**Programmatic Integration:**
```python
from advanced_gui.calculator_advanced import CalculatorGUI
import tkinter as tk

# Embed in larger application
root = tk.Tk()
calc_frame = tk.Frame(root)
calc = CalculatorGUI(master=calc_frame)
calc_frame.pack()
root.mainloop()
```

**Keyboard Shortcuts (GUI):**
- `Enter` / `Return`: Evaluate expression
- `Escape`: Clear current input
- `Backspace`: Delete last character
- `Numbers` and `Operators`: Direct input

### Advanced Usage Examples

**Batch Processing:**
```python
# Process multiple calculations
expressions = ["10 + 5", "20 * 3", "100 / 4"]
for expr in expressions:
    result = safe_eval(expr)
    print(f"{expr} = {result}")
```

**History Export:**
```python
# Export calculation history to CSV
import csv
from advanced_gui.calculator_advanced import read_history

history = read_history()
with open('calculations.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Expression', 'Result'])
    for line in history:
        if ' = ' in line:
            expr, result = line.split(' = ', 1)
            writer.writerow([expr, result])
```

---

## 📸 Screenshots & Demo

### CLI Calculator Interface
```
📷 [Screenshot Placeholder: CLI Menu Interface]
```
*Simple, text-based interface perfect for terminal environments*

### GUI Calculator Interface
```
📷 [Screenshot Placeholder: GUI Calculator Window]
```
*Modern Tkinter interface with button grid and history panel*

### History Management
```
🎥 [GIF Placeholder: History Navigation Demo]
```
*Demonstration of saving, viewing, and reusing calculations*

### Advanced Features
```
🎥 [GIF Placeholder: Complex Expression Evaluation]
```
*Complex mathematical expressions with parentheses and operators*

---

## 🤝 Contributing

**We welcome contributions from developers of all skill levels!**

### Quick Contribution Guide

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/yourusername/calculator-project.git
   ```
3. **Create** a feature branch:
   ```bash
   git checkout -b feature/your-amazing-feature
   ```
4. **Make** your changes and **test** thoroughly:
   ```bash
   pytest tests/
   black .
   flake8 .
   ```
5. **Commit** with clear messages:
   ```bash
   git commit -m "Add scientific notation support"
   ```
6. **Push** and **create** a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black flake8 sphinx

# Run the full development pipeline
make test      # or pytest tests/
make format    # or black .
make lint      # or flake8 .
make docs      # or sphinx-build docs/ docs/_build/
```

### Contribution Areas

- 🐛 **Bug fixes** and error handling improvements
- ✨ **New features** (scientific functions, themes, export options)
- 📚 **Documentation** improvements and examples
- 🧪 **Test coverage** expansion
- 🎨 **UI/UX** enhancements
- 🚀 **Performance** optimizations

See our [Contributing Guidelines](CONTRIBUTING.md) for detailed information.

---

## 📄 License

**MIT License** - This project is open source and freely available.

Copyright (c) 2024 Calculator Project Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

See the [LICENSE](LICENSE) file for the complete license text.

---

## 🙏 Acknowledgments

### Inspiration & Goals
- **Educational Focus**: Inspired by the need for clear, practical Python learning examples
- **Community-Driven**: Built with input from Python learners and educators
- **Open Source Philosophy**: Committed to free, accessible programming education

### Technical Foundations
- **Python Standard Library**: Built entirely with Python's included modules
- **Tkinter GUI Framework**: Leveraging Python's built-in GUI toolkit
- **AST Safe Evaluation**: Using Python's Abstract Syntax Tree for secure expression evaluation

### Community
- Contributors who have helped improve the codebase
- Beta testers who provided valuable feedback
- Python community for ongoing support and inspiration

**Special thanks to everyone who has contributed to making this project better!**

---

## 📚 Documentation Links

### Per-Version Documentation
- **[CLI Calculator Documentation](beginner-cli/docs/)** - Complete guide for the command-line version
- **[GUI Calculator Documentation](advanced-gui/docs/)** - Comprehensive GUI version documentation
- **[API Reference](docs/api-reference.md)** - Detailed API documentation for both versions

### Additional Resources
- **[Getting Started Guide](docs/getting-started.md)** - Step-by-step setup and first steps
- **[Examples Collection](examples/)** - Code examples and demo scripts
- **[Developer Guide](docs/developer-guide.md)** - Advanced development topics
- **[FAQ](docs/faq.md)** - Frequently asked questions

### External Resources
- [Python Official Documentation](https://docs.python.org/)
- [Tkinter Tutorial](https://tkdocs.com/)
- [Python AST Documentation](https://docs.python.org/3/library/ast.html)

---

## 📞 Support & Community

### Getting Help
- 📖 **Documentation**: Check our [comprehensive docs](docs/)
- 🐛 **Bug Reports**: [Open an issue](https://github.com/yourusername/calculator-project/issues)
- 💡 **Feature Requests**: [Request a feature](https://github.com/yourusername/calculator-project/issues/new?template=feature_request.md)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/yourusername/calculator-project/discussions)

### Community Guidelines
- Be respectful and inclusive
- Help others learn and grow
- Share knowledge and experiences
- Follow our [Code of Conduct](CODE_OF_CONDUCT.md)

---

**Made with ❤️ for Python learners everywhere**

*Happy Calculating! 🧮✨*
