from collections import deque

class History:
    def __init__(self):
        self.calculations = deque(maxlen=5)
        
    def add_calculation(self, calculation):
        """Add a calculation to history"""
        self.calculations.append(calculation)
        
    def get_history(self):
        """Get list of previous calculations"""
        return list(self.calculations)
        
    def clear_history(self):
        """Clear calculation history"""
        self.calculations.clear()
