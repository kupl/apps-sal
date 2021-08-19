test = int(input())
for i in range(test):
    (items, given) = [int(x) for x in input().split()]
    weight = [int(y) for y in input().split()]
    weight.sort()
    (mn, mx) = (0, 0)
    if given <= items // 2:
        for j in range(1, items + 1):
            if j <= given:
                mn = mn + weight[j - 1]
            else:
                mx = mx + weight[j - 1]
        print(mx - mn)
    else:
        for j in range(1, items + 1):
            if j <= given:
                mn = mn + weight[items - j]
            else:
                mx = mx + weight[items - j]
        print(mn - mx)
