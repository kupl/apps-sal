for _ in range(int(input())):
    n, k = [int(kk) for kk in input().strip().split(" ")]
    a = [int(kk) for kk in input().strip().split(" ")]
    sm = max(a) + 50
    ts = [0] * (sm + 1)
    ts[sm] = 1
    for i in range(n):
        ts[a[i]] += 1
        ii = a[i]
        while ts[ii] == k:
            ts[ii] = 0
            ii += 1
            ts[ii] += 1
    tts, poss = ts[:], []
    for i in range(n):
        tts[a[i]] -= 2
        ii = a[i]
        while tts[ii] < 0:
            tts[ii] += k
            ii += 1
            tts[ii] -= 1
            if ii == sm:
                poss += [i]
                if i:
                    poss += [i - 1]
                    ptts = tts[:]
