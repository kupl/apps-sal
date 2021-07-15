for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l, r = 0, n-1
    com = False
    while l <= r:
        if a[l] == 0:
            l += 1
        if a[r] == 0:
            r -= 1
        elif a[l] != 0 and a[r] != 0:
            print(r-l+1)
            com = True
            break
    if not com:
        print(1)
