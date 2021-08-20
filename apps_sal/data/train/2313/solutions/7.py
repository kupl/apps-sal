n = int(input())
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
c = [0] * n
st = [0] * n
first = 0
second = 0
for i in range(1, n):
    while second - first > 0 and a[i] * b[st[first]] + c[st[first]] >= a[i] * b[st[first + 1]] + c[st[first + 1]]:
        first = first + 1
    c[i] = a[i] * b[st[first]] + c[st[first]]
    while second - first > 0 and (b[st[second]] - b[i]) * (c[st[second]] - c[st[second - 1]]) > (c[i] - c[st[second]]) * (b[st[second - 1]] - b[st[second]]):
        second = second - 1
    second = second + 1
    st[second] = i
print(c[n - 1])
