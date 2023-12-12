def basic_operations(a, b):
    result = {}
    try:
        result['addition'] = a + b
        result['subtraction'] = a - b
        result['multiplication'] = a * b
        result['division'] = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid input. Please provide numeric values for 'a' and 'b'.")
    return result


def power_operation(base, exponent, **kwargs):
    result = None
    try:
        result = base ** exponent
        if 'modulo' in kwargs:
            modulo = kwargs['modulo']
            result = result % modulo
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid input. Please provide numeric values for 'base' and 'exponent'.")
    return result


def apply_operations(operation_list):
    results = []
    for operation, args in operation_list:
        try:
            result = operation(*args)
            results.append(result)
        except Exception as e:
            print("Error:", str(e))
    return results
from math_operations import basic_operations, power_operation, apply_operations

result_basic = basic_operations(10, 5)
print("Basic Operations Result:", result_basic)

result_power = power_operation(2, 3)
print("Power Operation Result:", result_power)

result_power_modulo = power_operation(2, 3, modulo=5)
print("Power Operation with Modulo Result:", result_power_modulo)

operations = [
    (lambda x, y: x + y, (3, 4)),
    (lambda x, y: x * y, (2, 5)),
]

result_apply = apply_operations(operations)
print("Apply Operations Result:", result_apply)
Updated at 2023-12-12 22:42:24