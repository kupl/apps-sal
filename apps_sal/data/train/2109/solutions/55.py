import sys

def solve(a, b):
    ans = 0
    cur = int(a * b)

    left = 1
    right = cur + 1
    while left < right:
        mid = int((left + right)/2)
        z = int(mid/2)
        mx = z * (mid - z)
        if mx <= cur:
            ans = mid
            left = mid + 1
        else:
            right = mid

    if int(ans/2) * (ans - int(ans/2)) == cur and a != b:
        ans -= 1
    return ans

n = int(sys.stdin.readline())
for i in range(n):
    x = sys.stdin.readline()
    y = [int(z) for z in x.split()]
    print((max(int(solve(y[0], y[1]))-2, 0)))

