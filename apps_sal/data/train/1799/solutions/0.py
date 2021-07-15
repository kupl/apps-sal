def queens(fixQ, S):
    
    def areClashing(i,x):
        j,y = qs[i],qs[x]
        return j==y or abs(i-x)==abs(j-y)
    
    def dfs(i=0):
        if i==iQ:      return dfs(i+1)
        if i==len(qs): return 1
        
        for y in range(S):
            qs[i]=y
            if ( not any(areClashing(i,ii) for ii in range(i)) 
                 and (iQ<i or not areClashing(i,iQ))
                 and dfs(i+1) ): return 1
        
        
    iQ,yQ = ord(fixQ[0])-97, (int(fixQ[1]) or 10)-1
    qs    = [yQ if i==iQ else 0 for i in range(S)]
    dfs()
    return ','.join( f"{ chr(x+97) }{ str(y+1)[-1] }" for x,y in enumerate(qs))
