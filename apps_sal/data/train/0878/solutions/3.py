for i in range(int(input())):
    (N, K) = map(int, input().split())
    H = []
    H = [int(x) for x in input().split()]
    highest = 0
    count = 0
    for k in H:
        if k - highest > K:
            count = count + (k - highest - 1) // K
        highest = k
    print(count)
