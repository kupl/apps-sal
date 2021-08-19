try:
    # https://www.codechef.com/LTIME63B/problems/GHMC
    # Finally.... I properly understood what needs to be done.

    def ctlt(arr, val):
        # find number of values in sorted arr < val
        if arr[0] >= val:
            return 0
        lo = 0
        hi = len(arr)
        while hi - lo > 1:
            md = (hi + lo) // 2
            if arr[md] < val:
                lo = md
            else:
                hi = md

        return hi

    for _ in range(int(input())):
        n, k, x, d = map(int, input().split())
        z = input().strip().split()
        if k > 0:
            ps = list(map(int, z[:k]))
        else:
            ps = [x]

        ps.sort()

        if x < n or x < ps[-1] or n < k:
            print(-1)
            continue

        valchecked = 0
        fillval = 0
        valsdone = False
        isolbelow = True
        lastp = ps[0]

        while not valsdone and n >= k:
            if n == k:
                lo = x + d + 1  # put out of range
            else:
                # find best maxfill (before val support)
                lo = 1
                hi = x + 1
                while hi - lo > 1:
                    md = (hi + lo) // 2
                    v = (x - md + 1) + ctlt(ps, md)
                    if v < n:
                        hi = md
                    else:
                        lo = md

            valsdone = True
            checkto = ctlt(ps, lo) - 1
            if checkto >= valchecked:
                # support all vals
                for p in ps[valchecked + 1:checkto + 1]:
                    if lastp + d >= p:
                        isolbelow = False
                    elif isolbelow:
                        valsdone = False
                        fillval += lastp + d
                        n -= 1
                        isolbelow = (p > lastp + 2 * d)
                    else:
                        isolbelow = True
                    lastp = p
                valchecked = checkto
                if valsdone and isolbelow:
                    # check gap to maxfill
                    if lastp + d >= lo:
                        isolbelow = False
                    else:
                        valsdone = False
                        fillval += lastp
                        ps[checkto] += d
                        lastp += d
                        isolbelow = False
                        n -= 1

        if k > n:
            print(-1)
        elif k == n:
            print(sum(ps) + fillval)
        elif k == n - 1 and lo > ps[-1]:
            print(sum(ps) + fillval + min(x, ps[-1] + d))
        else:
            tot = (x + lo) * (x - lo + 1) // 2 + sum(ps[:ctlt(ps, lo)])
            print(tot + fillval)
except:
    pass
