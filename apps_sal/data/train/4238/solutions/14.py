def squares_needed(grains):
    if grains==0:
        return 0
    stop=1
    sum=1
    while sum<grains:
        sum=sum+(2**stop)
        stop+=1
    return stop
