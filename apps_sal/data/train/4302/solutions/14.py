def better_than_average(x,y):
    m=sum(x)
    a=(m/len(x))
    if a>=y:
        return False
    elif a<y:
        return True
