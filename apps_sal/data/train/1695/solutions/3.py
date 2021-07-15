ans = []
for i in range(1, 1001):
    ans.append(' '.join((str(i), '1', str(i), '2')))
ans.append('1 1 1 2')
for i in range(1, 1001):
    ans.append(' '.join((str(i), '1', str(i), '2')))

print(len(ans))
print('\n'.join(ans))

