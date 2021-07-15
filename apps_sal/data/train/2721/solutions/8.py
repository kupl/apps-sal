def pyramid(n):
    if n==0: return '\n'
    s=''
    t=0
    while n>1:
        s += ' '*(n-1) + '/' + ' '*(t) + '\\\n'
        n -= 1
        t += 2
    s += '/'+'_'*t+'\\\n'
    return s
