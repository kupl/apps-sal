for _ in range(int(input())):
    i = 0
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    so = l[i]
    result = sum(l)
    r = result // k
    if(r <= k):
        print(r + 1)
    else:
        print(r + k // so + 1)
