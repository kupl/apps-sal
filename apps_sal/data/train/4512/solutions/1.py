M = [0]

while len(M) <= 500:
        k, s = 0, {c for c in str(M[-1])}
        while k in M or {c for c in str(k)} & s:
            k += 1
        M.append(k)

find_num = lambda n: M[n]
