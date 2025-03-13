import math

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
