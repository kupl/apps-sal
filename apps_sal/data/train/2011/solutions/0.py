n = int(input())
q = []
for i in range(max(0, n - 100), n + 1):
    j = i
    res = i
    while j:
        res += j % 10
        j //= 10
    if res == n:
        q.append(i)
print(len(q))
for i in q:
    print(i)
