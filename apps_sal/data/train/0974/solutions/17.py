for _ in range(int(input())):
    a, b, c, d = list(map(int, input().split()))
    st = "YES"
    sad, spr = 0, 0
    if a == b:
        st = "YES"
    elif a > b:
        sad, spr = max(c, d), min(c, d)
        if sad == spr:
            st = "NO"
        else:
            if (a - b) % (sad - spr) == 0:
                st = "YES"
            else:
                st = "NO"
    else:
        sad, spr = min(c, d), max(c, d)
        if sad == spr:
            st = "NO"
        else:
            if (-a + b) % (-sad + spr) == 0:
                st = "YES"
            else:
                st = "NO"
    print(st)
