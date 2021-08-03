az = 'abcdefghijklmnopqrstuvwxyz'
for _ in range(int(input())):
    s = ''
    a = int(input())
    while 1:
        s = az[a::-1] + s
        if a < 26:
            break
        a = a - 25
    print(s)
