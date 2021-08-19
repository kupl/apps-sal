def arithmetic(a, b, operator):
    map_func = {'add': lambda a, b: a + b, 'subtract': lambda a, b: a - b, 'multiply': lambda a, b: a * b, 'divide': lambda a, b: a / b}
    return map_func[operator](a, b)
