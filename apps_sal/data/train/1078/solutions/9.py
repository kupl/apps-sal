for _ in range(int(input())):
    n = list(map(int, input().split()))
    s = n[0]
    w = n[1:]
    c = 0
    for i in range(3):
        if sum(w) <= s:
            c = c + 1
            break
        elif sum(w[:2]) <= s:
            w = w[2:]
            c = c + 1
        else:
            w = w[1:]
            c += 1
    print(c)
