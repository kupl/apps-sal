from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    fr, to = map(int, input().split())
    edges[fr].append(to)
    edges[to].append(fr)

order = []
parent = [-1] * (N + 1)
st = [1]
while st:
    now = st.pop()
    order.append(now)
    if now > 0:
        st.append(-now)
        for to in edges[now]:
            if to == parent[now]:
                continue
            st.append(to)
            parent[to] = now

L = [-10**18]
ans = [-1] * (N + 1)
st = [(-1, -1)] * (N + 1)

for now in order:
    if now < 0:
        val, idx = st[-now]
        if val == -1:
            L.pop()
        if val > 0:
            L[idx] = val
        continue

    a = A[now - 1]
    i = bisect_left(L, a)

    if len(L) == i:
        L.append(a)
    else:
        st[now] = (L[i], i)
        if L[i] > a:
            L[i] = a

    ans[now] = len(L) - 1

print(*ans[1:], sep='\n')

