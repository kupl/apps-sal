n = int(input())
a = [int(x) for x in input().split()]

s = 0
for i in range(n):
    s = s ^ a[i]

for i in range(n):
    x = s ^ a[i]
    print(x, end='')
    if i == n - 1:
        print('')
    else:
        print(' ', end='')
