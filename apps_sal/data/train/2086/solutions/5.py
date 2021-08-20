[n, q] = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
start = 0
end = n - 1
res = [-1 for i in range(n + 1)]
r = None
t = 0
M = max(a)
for i in range(n):
    if a[start] == M:
        if start > end:
            r = a[start + 1:] + a[:end + 1]
        else:
            r = a[start + 1:end + 1]
        t = i
        break
    [A, B] = [a[start], a[(start + 1) % n]]
    res[i] = [A, B]
    if A > B:
        (a[start], a[(start + 1) % n]) = (a[(start + 1) % n], a[start])
    start = (start + 1) % n
    end = (end + 1) % n
output = []
for x in range(q):
    m = int(input()) - 1
    if m >= t:
        output.append([M, r[(m - t) % len(r)]])
    else:
        output.append(res[m])
for i in output:
    print(i[0], i[1])
