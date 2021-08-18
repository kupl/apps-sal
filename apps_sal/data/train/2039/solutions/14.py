def chek(mid):
    v = 0
    for i in range(n):
        if (v - a[i]) % m > mid:
            if a[i] > v:
                v = a[i]
            else:
                return False
    return True


n, m = list(map(int, input().split()))

l = -1
r = m

a = list(map(int, input().split()))

chek(3)


while l < r - 1:

    mid = (l + r) // 2
    if chek(mid):
        r = mid
    else:
        l = mid

print(r)
