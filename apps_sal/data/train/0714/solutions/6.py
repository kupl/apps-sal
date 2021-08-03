t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    if total % n != 0:
        new_total = int(n * (int(total / n) + 1))
    else:
        new_total = total
    cand = new_total // n
    op = new_total - total

    for j in a:
        if j > cand:
            op += (j - cand)
    print(op)
