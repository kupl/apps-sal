for _ in range(int(input())):
    (n, k) = map(int, input().split())
    lst = list(map(int, input().split()))
    p = 0
    ele = 0
    for i in range(n - k + 1):
        x = lst[i:i + k]
        d = sum(x)
        dic = {j for j in set(x)}
        elm = len(dic)
        if elm >= ele:
            if ele > ele:
                p = d
            elif d > p:
                p = d
            ele = elm
    print(p)
