N = int(input())
a = list(map(int, input().split()))
res = [0 for i in range(N + 1)]
st = [(0, -1)]
for (i, hh) in enumerate(a):
    while st[-1][0] >= hh:
        num = st[-1][0]
        st.pop()
        ll = i - st[-1][1] - 1
        res[ll] = max(res[ll], num)
    st.append((hh, i))
while len(st) > 1:
    num = st[-1][0]
    st.pop()
    ll = N - st[-1][1] - 1
    res[ll] = max(res[ll], num)
for i in range(N - 1, 0, -1):
    res[i] = max(res[i], res[i + 1])
print(' '.join(map(str, res[1:])))
