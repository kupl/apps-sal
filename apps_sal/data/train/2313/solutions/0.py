n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [0] * n
stk = [0]
for i in range(1, n):
    while len(stk) > 1 and c[stk[1]] - c[stk[0]] <= a[i] * (b[stk[0]] -
            b[stk[1]]):
        del stk[0]
    c[i] = c[stk[0]] + a[i] * b[stk[0]]
    while len(stk) > 1 and ((c[stk[-1]] - c[stk[-2]]) * (b[stk[-1]] - b[i]) >
            (b[stk[-2]] - b[stk[-1]]) * (c[i] - c[stk[-1]])):
        del stk[-1]
    stk.append(i)
print(c[n - 1])

