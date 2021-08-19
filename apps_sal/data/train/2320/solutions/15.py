n = int(input())


def inp():
    return [*list(map(int, input().split()))]


a = sorted(inp(), reverse=True)
b = inp()
c = sorted([(i, b[i]) for i in range(n)], key=lambda x: x[1])
ans = [''] * n
for i in range(n):
    ans[c[i][0]] = str(a[i])
print(' '.join(ans))
