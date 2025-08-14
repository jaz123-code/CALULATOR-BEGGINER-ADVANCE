HISTORY_FILE = 'History.txt'

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()
        if len(lines) == 0:
            print("No history found")
        else:
            for line in reversed(lines):
                print(line.strip())
    except FileNotFoundError:
        print("No history file found")

def clear_history():
    with open(HISTORY_FILE, 'w') as file:
        pass
    print("History cleared")

def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(equation + " = " + str(result) + "\n")
    print("Result saved to history")

def calculate():
    equation = input("Enter the equation to calculate: ")
    try:
        result = eval(equation)
        print("Result:", result)
        save_to_history(equation, result)
    except Exception as e:
        print("Error:", e)

def main():
    print("Welcome to the calculator with history feature!")
    while True:
        print("1. CALCULATE  2. SHOW HISTORY  3. CLEAR HISTORY  4. EXIT")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter a valid number")
            continue

        if choice not in range(1, 5):
            print("Enter a valid choice")
            continue

        if choice == 1:
            calculate()
        elif choice == 2:
            show_history()
        elif choice == 3:
            clear_history()
        elif choice == 4:
            print("Exiting...")
            break

main()

    
    