t = int(input())
for _ in range(t):
    a = int(input())
    (d_max, max_d) = (1, 0)
    (chef, friend) = (0, 0)
    max_sum = 0
    while 1:
        chef += a
        friend += 2 ** (d_max - 1)
        if chef - friend > max_sum:
            max_sum = chef - friend
            max_d = d_max
        if chef - friend <= 0:
            break
        else:
            d_max += 1
    print(d_max - 1, max_d)
