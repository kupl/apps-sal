(n, m) = map(int, input().split())
a = set(map(int, input().split()))
y = 2 ** n
mk = [0] * (2 * y)
cur = 0
for x in a:
    if mk[x]:
        continue
    mk[x] = 1
    st = [x]

    def push(v):
        if not mk[v]:
            mk[v] = 1
            st.append(v)
    while st:
        u = st.pop()
        if u < y:
            push(y + u)
        else:
            for b in range(n):
                v = u | 1 << b
                push(v)
            v = y - 1 - (u - y)
            if v in a:
                push(v)
    cur += 1
print(cur)
