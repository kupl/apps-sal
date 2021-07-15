input()
print('\n'.join(['Infinite' if p * pow(b, 99, q) % q else 'Finite' for p, q, b in [list(map(int, l.split())) for l in __import__('sys').stdin.readlines()]]))

