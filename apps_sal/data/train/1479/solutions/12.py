for _ in range(int(input())):
    n = int(input())
    res = [0] * 9
    for i in range(n):
        (p, s) = map(int, input().split())
        if 1 <= p <= 8:
            if res[p] < s:
                res[p] = s
    print(sum(res))
