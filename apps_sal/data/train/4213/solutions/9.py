def array_info(x):
    return [[len(x) or None], [sum((isinstance(n, int) for n in x)) or None], [sum((isinstance(n, float) for n in x)) or None], [sum((isinstance(n, str) and n != ' ' for n in x)) or None], [sum((n == ' ' for n in x)) or None]] if x else 'Nothing in the array!'
