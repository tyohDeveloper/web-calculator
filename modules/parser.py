import ast
import operator

class ExpressionParser:
    def __init__(self):
        self.operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.Mod: operator.mod,
            ast.USub: operator.neg,
        }
    
    def parse(self, expr):
        """Parse and evaluate a mathematical expression"""
        try:
            # Convert string to AST
            tree = ast.parse(expr, mode='eval')
            # Evaluate AST
            result = self._evaluate(tree.body)
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")
    
    def _evaluate(self, node):
        """Recursively evaluate an AST node"""
        # Handle numbers
        if isinstance(node, ast.Num):
            return node.n
        
        # Handle unary operations (like -5)
        elif isinstance(node, ast.UnaryOp):
            op = self.operators.get(type(node.op))
            if op is None:
                raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")
            return op(self._evaluate(node.operand))
        
        # Handle binary operations (like 2 + 3)
        elif isinstance(node, ast.BinOp):
            op = self.operators.get(type(node.op))
            if op is None:
                raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
            return op(self._evaluate(node.left), self._evaluate(node.right))
        
        # Handle parentheses
        elif isinstance(node, ast.Expression):
            return self._evaluate(node.body)
        
        else:
            raise ValueError(f"Unsupported expression type: {type(node).__name__}")
