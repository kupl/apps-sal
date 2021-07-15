def ulam_sequence(u0, u1, n):
    S0={u0+u1}
    S1=set()
    a=[u0, u1]
    c=a.append
    for k in range(2,n):
        m=min(S0)
        c(m)
        S0.discard(m)
        
        
    
        T={a[i]+a[k] for i in range(k)}
        S0,S1=S0^T-S1, S1|(S0&T)
        
    return a
