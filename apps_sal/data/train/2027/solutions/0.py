t = input()
a, b = [i for i, d in enumerate(t, 1) if d == 'l'], [i for i, d in enumerate(t, 1) if d == 'r']
a.reverse()
print('\n'.join(map(str, b)))
print('\n'.join(map(str, a)))
