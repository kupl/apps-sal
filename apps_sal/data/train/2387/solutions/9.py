n = int(input())
for i in range(n):
    num = int(input())
    ost = 0
    out = 0
    while num > 9:
        x = num % 10
        num -= x
        ost = num // 10
        out += num
        num = ost + x
    out += num
    print(out)
