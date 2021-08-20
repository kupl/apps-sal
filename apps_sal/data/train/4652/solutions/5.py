def score(n):
    return n if n < 2 else pow(2, int(__import__('math').log(n, 2)) + 1) - 1
