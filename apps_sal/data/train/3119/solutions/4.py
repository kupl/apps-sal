def pattern(n, y=1, *_):
    y = y if y>1 else 1
    s1 = '1'+ ' '*(2*n-3) + '1'
    s2 = '\n'+'\n'.join(' '*i+str(i+1)[-1]+' '*(2*n-2*i-3)+str(i+1)[-1]+' '*i for i in range(1,n-1))
    s3 = '\n'+' '*(n-1) +str(n)[-1]+' '*(n-1)+'\n'
    return '' if n<1 else s1+(s2+s3+s2[::-1]+s1)*y
