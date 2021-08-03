# cook your dish here
for _ in range(int(input())):
    N = int(input())

    A = [int(v) for v in input().split()]
    B = [int(v) for v in input().split()]
    minAB = min(min(A), min(B))
    h = {}
    for ele in A:
        if ele in h:
            h[ele][0] += 1
        else:
            h[ele] = [1, 0]

    for ele in B:
        if ele in h:
            h[ele][1] += 1
        else:
            h[ele] = [0, 1]

    # print(h)
    flag = 0
    res = 0
    AtoB, BtoA, swaps = [], [], []
    for k, v in h.items():
        if v[0] == v[1]:
            pass
        elif (v[0] + v[1]) % 2 != 0:
            res = -1
            flag = 1
            break
        else:
            b = abs(v[0] - v[1]) // 2
            if v[0] > v[1]:
                v[1] += b
                v[0] -= b
            else:
                v[0] += b
                v[1] -= b

            for c in range(b):
                swaps.append(k)
    if flag != 1:
        swaps.sort()
        swaps = swaps[:len(swaps) // 2]
        for ele in swaps:
            if ele <= 2 * minAB:
                res += ele
            else:
                res += 2 * minAB
    # print(swaps)
    print(res)
