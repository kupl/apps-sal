s = "abcdefghijklmnopqrstuvwxyz"
for _ in range(0, int(input())):
    n = int(input())
    a = ''
    while True:
        a = s[n::-1] + a
        if n < 26:
            break
        n = n - 25
    print(a)
