t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    w = list(map(int, input().split()))
    count = 0
    while w != []:
        w1 = []
        for i in range(n):
            if sum(w1) + w[i] <= k:
                w1.append(w[i])
            else:
                break
        if w1 == []:
            count = -1
            break
        else:
            w[:len(w1)] = []
            n -= len(w1)
            count += 1
    print(count)
