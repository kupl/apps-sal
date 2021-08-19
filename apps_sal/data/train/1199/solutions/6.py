# cook your dish here
# cook your dish here
t = int(input())
while t > 0:
    s, n = map(int, input().split())
    c = 0
    if s <= n:
        if s % 2 == 0:
            print("1")
        elif s == 1:
            print("1")
        else:
            print("2")
    else:
        if s % 2 != 0:
            c += 1
            s -= 1
        c += s // n
        if s % n == 0:
            print(c)
        else:
            print(c + 1)
    t -= 1
