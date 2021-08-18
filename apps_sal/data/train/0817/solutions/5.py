for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    l = len(li)
    res = li[0]
    for i in range(1, l):
        res = res ^ li[i]
    print(res)
