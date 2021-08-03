import bisect

for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    for j in range(int(input())):
        x, y = map(int, input().split())
        z = x + y
        nu = bisect.bisect(a, z)
        if nu > 0:

            if a[nu - 1] == z:
                print(-1)
            else:
                print(nu)
        else:
            print(0)
