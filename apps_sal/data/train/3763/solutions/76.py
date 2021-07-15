def calculator(x, y, op):
    try:
        int(x)
        int(y)
    except:
        return 'unknown value'
    
    return {
        '+': int(x) + int(y),
        '-': int(x) - int(y),
        '*': int(x) * int(y),
        '/': int(x) / int(y) if int(y) != 0 else 'unknown value'
    }.get(op, 'unknown value')
