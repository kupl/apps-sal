# cook your dish here
for i in range(int(input())):
    n = int(input())
    a = (n // 2) + 1
    l = a - 2
    for j in range(1, a + 1):
        space = j - 1
        print(' ' * space, end='')
        print('*')
    for j in range(a + 1, n + 1):
        space = l
        print(' ' * space, end='')
        print('*')
        l -= 1
