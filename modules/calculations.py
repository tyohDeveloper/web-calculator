import math
from math import factorial as math_factorial

class Calculator:
    def __init__(self):
        self.memory = 0

    def calculate(self, num1, num2, operation):
        """Perform calculation based on the operation"""
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError
            return num1 / num2
        elif operation == '%':
            return num1 % num2
        elif operation == '^':
            return num1 ** num2
        elif operation == 'sqrt':
            if num1 < 0:
                raise ValueError("Cannot calculate square root of negative number")
            return math.sqrt(num1)
        # Scientific Calculator Functions
        elif operation == 'sin':
            return math.sin(math.radians(num1))
        elif operation == 'cos':
            return math.cos(math.radians(num1))
        elif operation == 'tan':
            return math.tan(math.radians(num1))
        elif operation == 'asin':
            if abs(num1) > 1:
                raise ValueError("Domain error: input must be between -1 and 1")
            return math.degrees(math.asin(num1))
        elif operation == 'acos':
            if abs(num1) > 1:
                raise ValueError("Domain error: input must be between -1 and 1")
            return math.degrees(math.acos(num1))
        elif operation == 'atan':
            return math.degrees(math.atan(num1))
        elif operation == 'log':
            if num1 <= 0:
                raise ValueError("Cannot calculate logarithm of non-positive number")
            return math.log10(num1)
        elif operation == 'ln':
            if num1 <= 0:
                raise ValueError("Cannot calculate natural logarithm of non-positive number")
            return math.log(num1)
        elif operation == 'exp':
            return math.exp(num1)
        elif operation == 'abs':
            return abs(num1)
        elif operation == 'fact':
            if num1 < 0 or num1 != int(num1):
                raise ValueError("Factorial is only defined for non-negative integers")
            return math_factorial(int(num1))
        else:
            raise ValueError("Invalid operation")

    def store_memory(self, value):
        """Store a value in memory"""
        self.memory = value

    def recall_memory(self):
        """Recall value from memory"""
        return self.memory

    def clear_memory(self):
        """Clear memory"""
        self.memory = 0