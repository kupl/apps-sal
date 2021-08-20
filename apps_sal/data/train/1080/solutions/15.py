t = int(input())
for i in range(t):
    s = input()
    l = set(s)
    if len(l) == 2:
        print('YES')
    else:
        print('NO')
