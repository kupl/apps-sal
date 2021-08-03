# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    direc, lang = input().split()
    if direc == 'R':
        x = (n - x) + 1
    if lang == 'H':
        if x % 2 == 0:
            print(x, 'E')
        else:
            print(x, 'H')
    else:
        if x % 2 == 0:
            print(x, 'H')
        else:
            print(x, 'E')
