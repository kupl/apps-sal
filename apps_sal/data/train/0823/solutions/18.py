t = int(input())

POW = 1 << 4
for _ in range(t):
    nums = list(map(int, input().split(' ')))
    f = 1
    for k in range(POW):
        s = -1
        for i, j in enumerate(nums):
            f = 1 << i
            if f & k != 0:
                if s == -1:
                    s = 0
                s += j
        if s == 0:
            f = 0
            break
    print(['No', 'Yes'][f == 0])
