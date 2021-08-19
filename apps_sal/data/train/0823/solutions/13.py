for _ in range(int(input())):
    (a, b, c, d) = [int(x) for x in input().split()]
    ls = [a, b, c, d]
    f = 0
    for i in range(2 ** 4):
        s = 0
        arr = []
        for j in range(4):
            if i & 1 << j > 0:
                s += ls[j]
                arr.append(ls[j])
        if s == 0 and len(arr) > 0:
            print('Yes')
            f = 1
            break
    if f == 0:
        print('No')
