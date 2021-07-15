def count_red_beads(n):
    if n==1 or n==0:
        return 0
    elif n%2!=0:
        return (n-1)*2
    else:
        return(n*2)-2
