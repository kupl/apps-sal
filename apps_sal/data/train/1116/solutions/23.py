from collections import defaultdict


def SubArr(arr, n):
    ps = defaultdict(lambda: 0)
    res = 0
    cs = 0
    for i in range(0, n):
        cs += arr[i]
        if cs == 0:
            res += 1
        if cs in ps:
            res += ps[cs]
        ps[cs] += 1
    return res


try:
    n = int(input())
    arr = list(map(int, input().split()))
    ans = SubArr(arr, n)
    print(ans)
except EOFError:
    pass
