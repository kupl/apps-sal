def __starting_point():
    (N, Q) = list(map(int, input().strip().split()))
    d = {}
    for _ in range(N):
        (a, b) = input().strip().split()
        d[a] = b
    for _ in range(Q):
        text = input().strip()
        idx = text.rfind('.')
        if idx >= 0 and text[idx + 1:] in d:
            print(d[text[idx + 1:]])
        else:
            print('unknown')


__starting_point()
