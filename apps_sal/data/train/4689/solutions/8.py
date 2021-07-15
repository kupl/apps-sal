def create_report(A):
    B={}
    for a in A:
        if"Labrador Duck"in a:return ['Disqualified data']
        W=a.replace('-',' ').upper().split()
        c,L=int(W.pop()),len(W)
        n=L==1and W[0][:6]or L==2and W[0][:3]+W[1][:3] or L==3and W[0][:2]+W[1][:2]+W[2][:2]or W[0][0]+W[1][0]+W[2][:2]+W[3][:2]
        B[n]=B.get(n,0)+c
    return sum([[k,B[k]]for k in sorted(B)],[])
