(n, s) = map(int, input().split())
ar = list(map(int, input().split()))
ar.sort()
z = n // 2
q = 0
if ar[z] < s:
    for i in range(z, n):
        if ar[i] < s:
            q += s - ar[i]
        else:
            break
else:
    for i in range(z, -1, -1):
        if ar[i] > s:
            q += ar[i] - s
        else:
            break
print(q)
