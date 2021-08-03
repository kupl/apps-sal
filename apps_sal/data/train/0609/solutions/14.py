for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    result = sum(l)
    r = result // k
    print(r + 1)
