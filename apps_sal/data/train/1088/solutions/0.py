t = int(input())
while t:
    s = input().split()
    m = int(s[0])
    p = float(s[1])
    if m % 2 == 0:
        r = (1 - p ** m) / (p + 1)
    else:
        r = (1 + p ** m) / (p + 1)
    print(1000000000 * r, 1000000000 * (1 - r))
    t -= 1
