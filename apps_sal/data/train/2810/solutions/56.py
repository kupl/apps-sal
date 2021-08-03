def solve(arr):
    alph = range(ord('a'), ord('z') + 1)

    res = []
    for s in arr:
        sl = s.lower()
        val = 0
        for i in range(len(sl)):
            if i >= len(alph):
                break

            if ord(sl[i]) == alph[i]:
                val += 1
        res.append(val)
    return res
