def traffic_jam(m,S):
    M=list(m)
    for i in range(len(S))[::-1]:
        R=sum(zip(M[i:],S[i][::-1]),())
        M[i:]=list(R)+M[i+len(R)//2:]
    return''.join(M)[:M.index('X')+1]
