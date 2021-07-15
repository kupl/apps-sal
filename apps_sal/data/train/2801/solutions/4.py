def pattern(n,x=1,y=1,*args):
    lines=[]; x-=1
    for i in range(1,n+1):
        line=' '*(i-1)+str(i)[-1]+' '*(n-i)
        line+=line[-2::-1]
        line+=line[1:]*x        
        lines.append(line)
    pat=lines+lines[-2::-1]
    pat+=pat[1:]*(y-1)
    return '\n'.join(pat)

