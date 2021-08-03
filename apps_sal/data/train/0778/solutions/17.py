# cook your dish here
t = int(input())
while t > 0:
    n = int(input())
    tmp = int(n)
    r = 0
    while tmp > 0:
        d = int(tmp % 10)
        r = int(r * 10 + d)
        tmp = int(tmp / 10)
    print(r)
    t -= 1
