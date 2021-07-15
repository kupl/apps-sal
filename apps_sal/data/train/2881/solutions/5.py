def validate(n):
    x = [int(c) if not i%2 else int(c)*2 for i, c in enumerate(str(n)[::-1])]
    return sum([c if c<9 else c-9 for c in x]) % 10 == 0
