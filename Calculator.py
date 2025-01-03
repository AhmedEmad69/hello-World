import tkinter as tk

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: Division by zero")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle key presses
def key_press(event):
    if event.char.isdigit() or event.char in ".+-*/()":
        button_click(event.char)
    elif event.keysym == "Return":
        evaluate()
    elif event.keysym == "BackSpace":
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])

# Function to simulate button press for testing
def simulate_button_press(value):
    button_click(value)
    return entry.get()

# Setting up the main window
root = tk.Tk()
root.title("Cool Calculator")
root.geometry("400x600")
root.bind("<Key>", key_press)

# Entry widget for the input/output
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Creating buttons
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, command=evaluate)
    elif text == "C":
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, command=clear)
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2, command=lambda value=text: button_click(value))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the application
if __name__ == "__main__":
    root.mainloop()

# Testing the calculator functions
def test_calculator():
    # Basic operations
    assert simulate_button_press("2") == "2", "Test failed for button press: 2"
    assert simulate_button_press("+") == "2+", "Test failed for button press: +"
    assert simulate_button_press("2") == "2+2", "Test failed for button press: 2"
    simulate_button_press("=")
    assert entry.get() == "4", "Test failed for expression: 2+2"
    clear()
    assert entry.get() == "", "Test failed for clear function"

    # Multiplication
    simulate_button_press("9")
    simulate_button_press("*")
    simulate_button_press("3")
    simulate_button_press("=")
    assert entry.get() == "27", "Test failed for expression: 9*3"
    clear()

    # Division
    simulate_button_press("1")
    simulate_button_press("0")
    simulate_button_press("/")
    simulate_button_press("2")
    simulate_button_press("=")
    assert entry.get() == "5.0", "Test failed for expression: 10/2"
    clear()

    # Order of operations
    simulate_button_press("7")
    simulate_button_press("+")
    simulate_button_press("2")
    simulate_button_press("*")
    simulate_button_press("3")
    simulate_button_press("=")
    assert entry.get() == "13", "Test failed for expression: 7+2*3"
    clear()

    # Division by zero
    simulate_button_press("1")
    simulate_button_press("/")
    simulate_button_press("0")
    simulate_button_press("=")
    assert entry.get() == "Error: Division by zero", "Test failed for division by zero"
    clear()

    # Invalid input
    simulate_button_press("+")
    simulate_button_press("+")
    simulate_button_press("=")
    assert entry.get() == "Error", "Test failed for invalid input: ++"
    clear()

    # Empty input
    simulate_button_press("=")
    assert entry.get() == "Error", "Test failed for empty input"
    clear()

    print("All tests passed.")

test_calculator()
