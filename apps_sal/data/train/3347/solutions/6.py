def minimum(a, x):
    near = x
    while near < a:
        near += x
    plus = near - a
    minus = a - (near - x)
    return plus if plus < minus else minus
