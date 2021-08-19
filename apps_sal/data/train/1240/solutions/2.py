# cook your dish here
n = int(input())
for _ in range(n):
    m = int(input())
    lis = list(map(int, input().strip().split()))
    res = []
    for ele in lis:
        if ele % 6 == 0:
            res.append(6)
        res.append(ele % 6)
    print(sum(res))
