def automorphic(n):
    square = str(n * n)
    n = str(n)
    last_digits = square[-len(n):]
    if last_digits == n:
        return "Automorphic"
    return "Not!!"
