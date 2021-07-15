def count_red_beads(n):
    ecount = 2
    ocount = 4
    oplst1 = []
    
    if n < 2:
        return 0
    else:
        for i in range(2, n+1):
            if i % 2 == 0:
                oplst1.append(ecount)
                ecount += 4
            else:
                oplst1.append(ocount)
                ocount += 4
    
        return oplst1[-1]
