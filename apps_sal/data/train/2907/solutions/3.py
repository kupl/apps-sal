S = [[1]]
for n in range(1,1801):
    S.append([1])
    for k in range(1, n):
        S[n].append(S[n-1][k-1] + (k+1) * S[n-1][k])
    S[n].append(1)

def combs_non_empty_boxesII(n):
    tot, max, index = 0, 1, 1
    for ix in range(len(S[n-1])):
        val = S[n-1][ix]
        tot = tot + val
        if val >= max:
            max = val
            index = ix
    return [tot, max, index+1]
