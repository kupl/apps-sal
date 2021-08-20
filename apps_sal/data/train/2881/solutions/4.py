def validate(n):
    return not sum((sum(map(int, str(int(d) + i % 2 * int(d)))) for (i, d) in enumerate(str(n)[::-1]))) % 10
