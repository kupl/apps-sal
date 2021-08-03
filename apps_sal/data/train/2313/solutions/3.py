def read(): return map(int, input().split())


n = int(input())
a = list(read())
b = list(read())
dp = [0] * n
st = [0]


def f1():
    i0, i1 = st[0], st[1]
    b1 = dp[i1] - dp[i0]
    k1 = b[i0] - b[i1]
    return b1 <= a[i] * k1


def f2():
    i1, i2 = st[-1], st[-2]
    k1, k2 = b[i1] - b[i], b[i2] - b[i1]
    b1, b2 = dp[i] - dp[i1], dp[i1] - dp[i2]
    return b2 * k1 > b1 * k2


for i in range(1, n):
    while len(st) > 1 and f1():
        st.pop(0)
    dp[i] = dp[st[0]] + a[i] * b[st[0]]
    while len(st) > 1 and f2():
        st.pop()
    st.append(i)
print(dp[n - 1])
