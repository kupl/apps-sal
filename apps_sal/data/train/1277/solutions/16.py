t = int(input())

for _ in range(t):
    a = int(input())
    l = 0
    for _ in range(a):
        x, y, z = map(int, input().split())
        add_per = x + (x * (z / 100))
        act_prz = add_per * (z / 100)
        loss = add_per - act_prz
        act_lss = (x - loss) * y
        l += act_lss
    print("%0.7f" % l)
