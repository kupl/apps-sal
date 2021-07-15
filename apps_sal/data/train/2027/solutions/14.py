s = input()
a, b = [], []
for i, j in zip(s, range(1, len(s)+1)):
    if i == 'r': a.append(str(j))
    else: b.append(str(j))
print('\n'.join(a + b[::-1]))
