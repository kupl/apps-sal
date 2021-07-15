from itertools import cycle

def custom_christmas_tree(chars, n):
    space = lambda i=0: " " * (n - 1 - i)
    leaf = cycle(chars)
    body = [space(i) + " ".join(next(leaf) for _ in range(i+1)) for i in range(n)]
    body.extend([f"{space()}|" for _ in range(n//3)])
    return '\n'.join(body)
