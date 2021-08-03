def solve(a, b):
    A = sum(x > y for x, y in zip(a, b))
    B = sum(x < y for x, y in zip(a, b))
    winner, name = ('Alice', 'Kurt') if A > B else ('Bob', 'Jeff')
    return '{}, {}: that looks like a "draw"! Rock on!'.format(A, B) if A == B \
        else '{}, {}: {} made "{}" proud!'.format(str(A), str(B), winner, name)
