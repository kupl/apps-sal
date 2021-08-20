def solve(a, b):
    return sum((all((a + b in '69 96 88 11 00' for (a, b) in zip(str(i), str(i)[::-1]))) for i in range(a, b)))
