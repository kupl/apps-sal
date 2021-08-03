t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    p, q = input().split()
    char = ""
    pos = 0
    if p == "L":
        pos = k
    else:
        pos = n - k + 1
    if pos & 1 == 1:
        char = q
    else:
        if q == 'H':
            char = "E"
        else:
            char = "H"
    print(pos, char)
