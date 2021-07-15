def balanced_num(number):
    l=len(str(number))
    a=str(number)[:(l-1)//2]
    b=str(number)[l//2+1:]
    #return a,b
    if sum(int(i) for i in a)==sum(int(i) for i in b):
        return 'Balanced'
    return 'Not Balanced'
