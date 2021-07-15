def pattern(n):
    lines=[]
    for i in range(1,n+1):
        line=' '*(i-1)+str(i%10)+' '*(n-i)
        lines.append(line+line[-2::-1])
    return '\n'.join(lines+lines[-2::-1])
