for __ in range(int(input())):
    val = list(map(int, input().split()))
    s = 0
    for i in range(0, len(val) - 1):
        s += val[i] * val[-1]
    if s <= 24 * 5:
        print('No')
    else:
        print('Yes')
