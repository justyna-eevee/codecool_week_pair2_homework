def validate_number(number):
    try:
        int(number)
    except ValueError as e:
        print('ENTER NUMBER!!!')
        return None
    else:
        return True


def ask_for_a_number(function):
    while True:
        number_input = input('Please provide a number: ')
        if function(number_input):
            print(f'Entered a number {number_input}')
            return number_input


def is_valid_operator(operator):
    operators = ['-', '+', '/', '*']
    if operator in operators:
        print('Operator OK')
        return True
    print('Invalid operator')
    return False


def ask_for_a_operator(function):
    while True:
        operator_input = input('Please provide an operator + - / *: ')
        if function(operator_input):
            print(f'Entered an operator {operator_input}')
            return operator_input

def calc(operator, digit_a, digit_b):
    if int(digit_b) == 0 and operator == '/':
        return 'Error: Division by zero'
    if operator == '+':
        return int(digit_a) + int(digit_b)
    elif operator == '-':
        return int(digit_a) - int(digit_b)
    elif operator == '*':
        return int(digit_a) * int(digit_b)
    else:
        return int(digit_a) / int(digit_b)
    


def simple_calculator():
    digit_a = ask_for_a_number(validate_number)
    digit_b = ask_for_a_number(validate_number)
    operator = ask_for_a_operator(is_valid_operator)
    return calc(operator, digit_a, digit_b)


if __name__ == "__main__":
    print(f'The result is {simple_calculator()}')
