def count_red_beads(n):
    if n<2:
        return 0
    else:
        i =0
        RedCount = -2
    while(i<n):
        RedCount+=2
        i+=1
    return RedCount

