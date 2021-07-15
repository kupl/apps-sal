q,solve=lambda p:p==p[::-1],lambda s:any(q(s[x:]+s[:x])for x in range(len(s)))
