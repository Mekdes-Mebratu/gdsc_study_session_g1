def power_operation(base, exponent, **kwargs):
    result = base ** exponent

    if 'modulo' in kwargs:
        modulo = kwargs['modulo']
        result = result % modulo

    return result
result1 = power_operation(15, 7)
print(result1)  

result2 = power_operation(10, 8, modulo=3)
print(result2)  
Updated at 2023-12-12 22:42:24