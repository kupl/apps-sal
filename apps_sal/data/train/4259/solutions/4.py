def pattern(n, x=1, *_):
    x = x if x>1 else 1
    s1 = ''.join('1'+' '*(2*n-3) for i in range(x))+str(1)+'\n'
    s = '\n'.join((' '*i+str(i+1)[-1]+' '*(2*n-2*i-3)+str(i+1)[-1]+' '*(i-1))*x+' ' for i in range(1,n-1))
    s1 = s1 if s =='' else s1+s+'\n'
    s = s1+(' '*(n-1) +str(n)[-1]+' '*(n-2))*x+' '
    return '' if n<1 else s+s1[::-1]
