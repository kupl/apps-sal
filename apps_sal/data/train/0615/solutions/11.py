for u in range(int(input())):
    (n, k) = map(int, input().split())
    l = list(map(int, input().split()))
    for q in range(k):
        (x, y) = map(int, input().split())
        print(sum(l[x - 1:y]))
