def balanced_num(n):
    return '%sBalanced' % ( 'Not ' if (sum(int(e) for e in str(n)[:(len(str(n))+1)//2-1]) !=  sum(int(e) for e in str(n)[(len(str(n)))//2+1:])) else '' ) 
