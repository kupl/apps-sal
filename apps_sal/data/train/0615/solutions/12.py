for u in range(int(input())):
    (n, k) = list(map(int, input().split()))
    l = list(map(int, input().split()))
    for q in range(k):
        (x, y) = list(map(int, input().split()))
        s = 0
        for i in range(x - 1, y):
            s = s + l[i]
        print(s)
