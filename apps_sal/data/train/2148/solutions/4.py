input()
print('\n'.join([(lambda p, q, b: 'Infinite' if p * pow(b, 60, q) % q else 'Finite')(*x) for x in [list(map(int, l.split())) for l in __import__('sys').stdin.readlines()]]))

