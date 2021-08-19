n = int(input())
A = [int(i) for i in input().split()]
ans = 0
st = [0]
tdeath = [-1 for i in range(n)]
for i in range(1, n):
    tdeath[i] = 0
    while len(st) > 0 and A[st[-1]] < A[i]:
        tdeath[i] = max(tdeath[i], tdeath[st[-1]] + 1)
        st.pop()
    if len(st) == 0:
        tdeath[i] = -1
    st.append(i)
    ans = max(ans, tdeath[i] + 1)
print(ans)
