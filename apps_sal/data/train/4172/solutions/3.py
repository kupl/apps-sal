def solve(s):
    if len(s) % 2: return -1
    count, swap = 0, 0
    for i,c in enumerate(s):
        count += (c == '(') - (c == ')')
        if count < 0:
            swap += 1 ; count = 1
        elif count > len(s)-i: 
            swap += 1 ; count -= 2
    return swap
