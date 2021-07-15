MEMO = []

def sum_dif_rev(n):
    i = MEMO[-1] if MEMO else 0
    
    while len(MEMO) < n:
        i += 1
        r = int(str(i)[::-1])
        if i % 10 and r != i and (i + r) % abs(r - i) == 0:
            MEMO.append(i)

    return MEMO[n-1]
