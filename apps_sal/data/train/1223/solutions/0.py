t = int(input())


def vsense(val, a, l):
    sense = 0
    ctr = a
    for c in range(n):
        if val[c] <= ctr:
            sense += -1
        else:
            sense += 1
        ctr += l
    return sense


while t:
    (n, l, a, b) = list(map(int, input().split()))
    val = list(map(int, input().split()))
    val.sort()
    sense = 0
    if b == a + n * l or vsense(val, a, l) <= 0:
        loc = a
    else:
        st = a
        end = b - n * l
        while st <= end:
            m = (st + end) / 2
            chk = vsense(val, m, l)
            if chk == 0:
                loc = m
                break
            elif chk < 0:
                end = m - 1
            else:
                loc = m
                st = m + 1
    ans = 0
    st = loc
    for c in range(n):
        ans += abs(st - val[c])
        st += l
    print(ans)
    t -= 1
