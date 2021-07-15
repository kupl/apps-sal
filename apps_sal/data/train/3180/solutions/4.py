def trotter(n):
    digits = set()
    for i in range(n, 10 ** 10, n or 10 ** 10):
        digits.update(str(i))
        if len(digits) == 10:
            return i
    return 'INSOMNIA'
