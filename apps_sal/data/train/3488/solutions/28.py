def eval_object(operation):
    if operation['operation'] == '+':
        x = operation['a'] + operation['b']
    elif operation['operation'] == '-':
        x = operation['a'] - operation['b']
    elif operation['operation'] == '/':
        x = operation['a'] / operation['b']
    elif operation['operation'] == '*':
        x = operation['a'] * operation['b']
    elif operation['operation'] == '%':
        x = operation['a'] % operation['b']
    elif operation['operation'] == '**':
        x = operation['a'] ** operation['b']
    return x
