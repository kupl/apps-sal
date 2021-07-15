def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())

n = ii()
a = list(map(int, list(input().strip())))
b = list(map(int, list(input().strip())))

o = [0, 0]
z = [0, 0]
for i in range(n):
    if a[i]:
        o[b[i]] += 1
    else:
        z[b[i]] += 1

ans = z[0] * o[1] + z[1] * o[0] + z[0] * o[0]

print(ans)

