FOUND, n = {}, 1
while len(FOUND) < 60:
    sq = n**.5
    nDivs = sum(2*(not n%x) for x in range(1,int(sq)+1)) - (int(sq)==sq)
    if nDivs not in FOUND: FOUND[nDivs] = n
    n += 1
    
def find_min_num(nDivs): return FOUND[nDivs]
