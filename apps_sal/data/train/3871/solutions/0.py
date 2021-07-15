def binary_simulation(s, q):
    out,n,s = [],int(s,2),len(s)
    for cmd,*i in q:
        if cmd=='I':
            a,b=i
            n ^= (1<<b-a+1)-1<<s-b
        else:
            out.append( str(int(0 < 1<<s-i[0] & n )) )
    return out
