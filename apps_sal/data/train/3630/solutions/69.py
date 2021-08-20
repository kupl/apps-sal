def arithmetic(a, b, operator):
    ans = 0
    if operator == 'add':
        ans = a + b
    elif operator == 'subtract':
        ans = a - b
    elif operator == 'multiply':
        ans = a * b
    elif operator == 'divide':
        ans = a / b
    return ans
