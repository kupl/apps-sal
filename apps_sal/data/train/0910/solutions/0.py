t = int(input())
for i in range(t):
    C = [ord(x) - ord('R') for x in list(input())]
    N = int(input())
    L = sum(C)
    r = 1
    c = 0
    while(r * L < N * 12):
        c += N * 12 - r * L
        r += 1
    print(c)
