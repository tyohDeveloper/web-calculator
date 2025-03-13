from flask import Flask, render_template, request, redirect, url_for
from modules.calculations import Calculator
from modules.history import History
from modules.parser import ExpressionParser
import os
import signal
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
calculator = Calculator()
history = History()
parser = ExpressionParser()

@app.route('/')
def index():
    logger.info("Serving index page")
    return render_template('calculator.html', 
                         memory=calculator.memory,
                         history=history.get_history(),
                         result=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        if 'expression' in request.form:
            # Handle expression-based calculation
            expression = request.form['expression']
            logger.info(f"Processing expression: {expression}")
            result = parser.parse(expression)
            operation_str = f"{expression} = {result}"
        else:
            # Handle traditional calculator operation
            num1 = float(request.form['num1'])
            operation = request.form['operation']
            logger.info(f"Processing calculation: {num1} {operation}")

            if operation == 'sqrt':
                result = calculator.calculate(num1, 0, operation)
                operation_str = f"sqrt({num1}) = {result}"
            else:
                num2 = float(request.form['num2'])
                result = calculator.calculate(num1, num2, operation)
                operation_str = f"{num1} {operation} {num2} = {result}"

        history.add_calculation(operation_str)
        logger.info(f"Calculation result: {operation_str}")

        return render_template('calculator.html',
                             memory=calculator.memory,
                             history=history.get_history(),
                             result=result)
    except ValueError as e:
        logger.error(f"ValueError in calculation: {str(e)}")
        return render_template('calculator.html',
                             memory=calculator.memory,
                             history=history.get_history(),
                             result=f"Error: {str(e)}")
    except ZeroDivisionError:
        logger.error("Division by zero attempted")
        return render_template('calculator.html',
                             memory=calculator.memory,
                             history=history.get_history(),
                             result="Error: Cannot divide by zero!")
    except Exception as e:
        logger.error(f"Unexpected error in calculation: {str(e)}")
        return render_template('calculator.html',
                             memory=calculator.memory,
                             history=history.get_history(),
                             result=f"Error: {str(e)}")

@app.route('/memory', methods=['POST'])
def memory_operation():
    action = request.form['action']
    logger.info(f"Memory operation requested: {action}")

    if action == 'store':
        try:
            value = float(request.form['value'])
            calculator.store_memory(value)
            logger.info(f"Stored value in memory: {value}")
        except ValueError:
            logger.error("Invalid value for memory storage")
            pass
    elif action == 'recall':
        recalled_value = calculator.recall_memory()
        logger.info(f"Recalled value from memory: {recalled_value}")
        return render_template('calculator.html',
                             memory=calculator.memory,
                             history=history.get_history(),
                             result=f"Recalled: {recalled_value}")
    elif action == 'clear':
        calculator.clear_memory()
        logger.info("Memory cleared")

    return redirect(url_for('index'))

@app.route('/quit', methods=['POST'])
def quit():
    logger.info("Quit requested - shutting down server")
    # Gracefully shutdown the server
    os.kill(os.getpid(), signal.SIGTERM)
    return "Calculator shutting down...", 200

if __name__ == '__main__':
    # ALWAYS serve the app on port 5000
    app.run(host='0.0.0.0', port=5000)