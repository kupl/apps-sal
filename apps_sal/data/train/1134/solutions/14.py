t = eval(input())
while t:
    t -= 1
    a, b = [int(x) for x in input().split()]
    s = [int(x) for x in input().split()]
    r = sum(s[0:b])
    for x in range(b, a):
        r = r - s[x] / 2
    if r < 0:
        print("DEFEAT")
    else:
        print("VICTORY")
