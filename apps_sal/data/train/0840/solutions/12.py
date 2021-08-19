def f(n):
    if n == 1:
        print('*')
        return
    if n == 2:
        print('*')
        print('*')
        return
    k = n // 2
    j = 2
    print('*')
    while j <= k:
        print(j * ' ' + '*')
        j += 1
    while j > 1:
        print(j * ' ' + '*')
        j -= 1
    print('*')
    return


t = int(input())
for i in range(t):
    n = int(input())
    f(n)
