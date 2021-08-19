a = int(input())
for i in range(a):
    (b, c) = [int(b) for b in input().split()]
    for r in range(b + c + 1, 3001):
        s = 0
        for t in range(2, r):
            if r % t == 0:
                s += 1
        if s == 0:
            print(r - b - c)
            break
