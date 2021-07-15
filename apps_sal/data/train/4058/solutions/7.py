def pattern(n):
    s = '\n'.join(' '*i+str(i+1)[-1]+' '*(2*n-1-2*(i+1))+str(i+1)[-1]+' '*i for i in range(n-1))
    s1= '\n'+' '*(n-1) +str(n)[-1]+' '*(n-1)+'\n'
    return '' if n<1 else s+s1+s[::-1]
