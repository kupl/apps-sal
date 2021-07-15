def check(k, a, b):
    i = (k-a)//2
    return -(i+a)*(i-k) < a*b

q = int(input())
for i in range(q):
    a,b = map(int, input().split())
    if a == b:
        print(2*a-2)
        continue
    a,b = sorted([a,b])
    ans = a-1
    left = a
    right = 10**9

    while right-left > 1:
        mid = (right+left)//2
        if check(mid, a, b):
            left = mid
        else:
            right = mid
    ans += left-1
    print(ans)
