T = eval(input())
arr = list(map(int, input().split(' ')))
x = set()
y = set(arr)
for i in range(T):
    x.add(i + 1)
for i in x.difference(y):
    print('{0}'.format(i), end=' ')
print('')
