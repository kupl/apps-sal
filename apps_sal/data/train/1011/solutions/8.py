for _ in range(int(input())):
    (N, K) = map(int, input().split())
    s = input()
    c = 0
    for i in range(N):
        if s[i].islower():
            c += 1
    if K >= c and K >= N - c:
        print('both')
    elif c >= K and N - c <= K:
        print('chef')
    elif c <= K and N - c >= K:
        print('brother')
    else:
        print('none')
