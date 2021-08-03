T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    w = list(map(int, input().split()))
    if max(w) <= K:
        x = y = 0
        for i in range(len(w)):
            x += w[i]
            if x > K:
                y += 1
                x = w[i]
        if x > 0:
            y += 1
        print(y)
    else:
        print("-1")
