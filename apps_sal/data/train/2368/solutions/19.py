t = int(input())
for T in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    minA = min(a)
    minB = min(b)

    moves = 0
    for g in range(n):
        moves += max(a[g] - minA, b[g] - minB)

    print(moves)
