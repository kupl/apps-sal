def check(w, x, n):
    if w == 0:
        return True
    if n == 0 and w != 0:
        return False
    if x[n - 1] > w:
        return check(w, x, n - 1)
    return check(w, x, n - 1) or check(w - x[n - 1], x, n - 1)


(n, qN) = list(map(int, input().rstrip().split()))
data = [int(i) for i in input().rstrip().split()]
for Q in range(qN):
    q = [int(i) for i in input().rstrip().split()]
    if q[0] == 1:
        data[q[1] - 1] = q[2]
    elif q[0] == 2:
        (i, j) = (q[1] - 1, q[2] - 1)
        new = data[:i] + data[i:j + 1][::-1] + data[j + 1:]
        data = new
    else:
        print('Yes' if check(q[3], data[q[1] - 1:q[2]], q[2] - q[1] + 1) else 'No')
