import os
import platform
import tkinter as tk
from tkinter import simpledialog, messagebox

class Display:
    def __init__(self):
        """Initialize root window for dialogs"""
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window

    def clear_screen(self):
        """Clear the console screen"""
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def show_menu(self):
        """Display the main menu"""
        print("\n=== Calculator ===")
        print("Available operations:")
        print("+ : Addition")
        print("- : Subtraction")
        print("* : Multiplication")
        print("/ : Division")
        print("% : Modulus")
        print("^ : Power")
        print("sqrt : Square Root")
        print("\nSpecial Commands:")
        print("h : Help")
        print("c : Clear Screen")
        print("m : Store in Memory")
        print("r : Recall from Memory")
        print("mc : Clear Memory")
        print("q : Quit")

    def show_help(self):
        """Display help information"""
        messagebox.showinfo("Help", 
            "1. Enter an operation from the available options\n"
            "2. Input the required numbers when prompted\n"
            "3. Use memory functions to store and recall values:\n"
            "   - 'm' to store a number in memory\n"
            "   - 'r' to recall the stored number\n"
            "   - 'mc' to clear the memory\n"
            "4. View the last 5 calculations in history\n"
            "5. Use 'c' to clear the screen\n"
            "6. Use 'q' to quit the calculator"
        )

    def show_memory(self, memory_value):
        """Display current memory value"""
        print(f"\nMemory: {memory_value}")

    def show_history(self, history):
        """Display calculation history"""
        print("\nLast 5 calculations:")
        for calc in history:
            print(calc)

    def get_operation(self):
        """Get operation from user via dialog"""
        return simpledialog.askstring("Operation", "Enter operation (or 'h' for help):", parent=self.root)

    def get_number(self, prompt):
        """Get number from user via dialog"""
        while True:
            try:
                num = simpledialog.askfloat("Input", prompt, parent=self.root)
                if num is None:  # User clicked Cancel
                    return None
                return num
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number!")

    def show_result(self, result):
        """Show calculation result"""
        messagebox.showinfo("Result", f"Result: {result}")

    def show_error(self, message):
        """Show error message"""
        messagebox.showerror("Error", message)