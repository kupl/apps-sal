def woow(l, oned):
    if 1 in l:
        return False
    else:
        for i in range(2, len(l) - 1):
            if (l.count(i) > oned):
                lm = l.count(i) // i
                for tp in range(1, lm):
                    if i + tp in l:
                        return False
        return True


tc = int(input())
for tcc in range(1, tc + 1):
    chocs = int(input())
    oned = int(input())
    l = list(map(int, input().split()))
    if woow(l, oned) == True:
        print("Possible")
    else:
        print("Impossible")
