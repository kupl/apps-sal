# cook your dish here
for _ in range(int(input())):
    s, n = map(int, input().split())
    c = 0
    if s <= n or s == 1:
        if s % 2 == 0 or s == 1:
            print(1)
        else:
            print(2)
    else:
        while n > 0:
            if n > s:
                n = s if s % 2 == 0 else s - 1
            else:
                c += s // n
                s = s % n
                n = n - 2
        print(c + s)
