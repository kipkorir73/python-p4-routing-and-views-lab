from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:str_param>')
def print_string(str_param):
    print(str_param)
    return str_param

@app.route('/count/<int:int_param>')
def count(int_param):
    numbers = "\n".join(str(i) for i in range(1, int_param + 1))
    return numbers

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed."
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation."

    return f"Result: {result}"

if __name__ == '__main__':
    app.run(port=5555)
