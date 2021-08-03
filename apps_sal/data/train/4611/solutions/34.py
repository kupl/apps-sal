def animals(heads, legs):
    rem = legs - 2 * heads
    cow = rem / 2
    chk = heads - rem / 2
    if heads < 0 or legs < 0 or rem < 0 or rem % 2 or chk < 0:
        return 'No solutions'
    else:
        return (chk, cow)
