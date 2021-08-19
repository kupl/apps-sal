n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [0] * n
st = [0]
for i in range(1, n):
    while len(st) > 1 and dp[st[0]] + b[st[0]] * a[i] > dp[st[1]] + b[st[1]] * a[i]:
        st.pop(0)
    dp[i] = dp[st[0]] + b[st[0]] * a[i]
    while len(st) > 1 and (dp[st[-2]] - dp[st[-1]]) * (b[st[-2]] - b[i]) < (dp[st[-2]] - dp[i]) * (b[st[-2]] - b[st[-1]]):
        st.pop()
    st.append(i)
print(dp[-1])
