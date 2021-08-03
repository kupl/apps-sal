for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    d = {}
    for ele in ar:
        if ele in d:
            d[ele] += 1
        else:
            d[ele] = 1
    m = 99999
    count = 0
    for ele in d:
        count += 1
        if m > d[ele]:
            m = d[ele]
    if count != 8:
        print(0)
    else:
        print(m)
