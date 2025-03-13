from modules.calculations import Calculator
from modules.history import History
import os
import platform
import math

class CalculatorCLI:
    def __init__(self):
        self.calculator = Calculator()
        self.history = History()
        self.running = True
        self.si_quality = 2  # Default to 2 decimal places

    def clear_screen(self):
        """Clear the console screen"""
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def display_menu(self):
        """Display the main menu"""
        print("\n=== Scientific Calculator ===")
        print("\nBasic Operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (^)")
        print("7. Square Root (sqrt)")
        
        print("\nScientific Operations:")
        print("8. Sine (sin)")
        print("9. Cosine (cos)")
        print("10. Tangent (tan)")
        print("11. Inverse Sine (asin)")
        print("12. Inverse Cosine (acos)")
        print("13. Inverse Tangent (atan)")
        print("14. Logarithm base 10 (log)")
        print("15. Natural Logarithm (ln)")
        print("16. Exponential (exp)")
        print("17. Absolute Value (abs)")
        print("18. Factorial (!)")
        
        print("\nMemory Operations:")
        print("m: Store in Memory")
        print("r: Recall from Memory")
        print("mc: Clear Memory")
        
        print("\nOther Operations:")
        print("h: View History")
        print("c: Clear Screen")
        print("q: Quit")
        print("s: SI Quality Settings")

    def format_number(self, number):
        """Format number according to SI quality setting"""
        return f"{number:.{self.si_quality}f}"

    def get_number(self, prompt):
        """Get a number from user input"""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number!")

    def handle_scientific_operation(self, operation):
        """Handle scientific calculator operations"""
        operations_map = {
            '1': ('+', True), '2': ('-', True), '3': ('*', True),
            '4': ('/', True), '5': ('%', True), '6': ('^', True),
            '7': ('sqrt', False), '8': ('sin', False), '9': ('cos', False),
            '10': ('tan', False), '11': ('asin', False), '12': ('acos', False),
            '13': ('atan', False), '14': ('log', False), '15': ('ln', False),
            '16': ('exp', False), '17': ('abs', False), '18': ('fact', False)
        }

        if operation not in operations_map:
            return

        op, needs_second_number = operations_map[operation]
        num1 = self.get_number("Enter first number: ")
        num2 = self.get_number("Enter second number: ") if needs_second_number else 0

        try:
            result = self.calculator.calculate(num1, num2, op)
            formatted_result = self.format_number(result)
            
            if needs_second_number:
                operation_str = f"{num1} {op} {num2} = {formatted_result}"
            else:
                operation_str = f"{op}({num1}) = {formatted_result}"
                
            print(f"\nResult: {formatted_result}")
            self.history.add_calculation(operation_str)
            
        except ValueError as e:
            print(f"\nError: {str(e)}")
        except ZeroDivisionError:
            print("\nError: Cannot divide by zero!")
        except Exception as e:
            print(f"\nError: {str(e)}")

    def set_si_quality(self):
        """Set SI quality (decimal places)"""
        print("\nSI Quality Levels:")
        print("1. Basic (1 decimal place)")
        print("2. Standard (2 decimal places)")
        print("3. High (3 decimal places)")
        print("4. Scientific (4 decimal places)")
        print("5. Ultra (5 decimal places)")
        
        while True:
            try:
                quality = int(input("\nEnter quality level (1-5): "))
                if 1 <= quality <= 5:
                    self.si_quality = quality
                    print(f"\nSI quality set to {quality} decimal places")
                    break
                else:
                    print("Please enter a number between 1 and 5")
            except ValueError:
                print("Please enter a valid number")

    def run(self):
        """Main program loop"""
        while self.running:
            self.display_menu()
            choice = input("\nEnter your choice: ").lower()

            if choice == 'q':
                print("\nThank you for using the calculator!")
                self.running = False
            elif choice == 'c':
                self.clear_screen()
            elif choice == 'h':
                print("\nCalculation History:")
                for calc in self.history.get_history():
                    print(calc)
            elif choice == 'm':
                value = self.get_number("Enter value to store: ")
                self.calculator.store_memory(value)
                print(f"Stored {self.format_number(value)} in memory")
            elif choice == 'r':
                value = self.calculator.recall_memory()
                print(f"Recalled value: {self.format_number(value)}")
            elif choice == 'mc':
                self.calculator.clear_memory()
                print("Memory cleared")
            elif choice == 's':
                self.set_si_quality()
            else:
                self.handle_scientific_operation(choice)

if __name__ == "__main__":
    calc = CalculatorCLI()
    calc.run()
