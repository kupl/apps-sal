def riders(sts, x):
    (st, x, back, n) = (0, x - 1, 0, 1)
    while True:
        (remain, back) = (100 - back, 0)
        while remain >= sts[st]:
            remain -= sts[st]
            st += 1
            if st == x:
                st -= 1
                x = -1
                back = sts[st]
                break
            elif st == len(sts):
                return n
        n += 1
