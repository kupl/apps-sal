
def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    S=input()
    T=input()
    
    N=len(S)
    M=len(T)
    
    sa=[0]*(N+1)
    for i in range(N):
        a=0
        if S[i]=="A":
            a=1
        sa[i+1]=sa[i]+a
        
    ta=[0]*(M+1)
    for i in range(M):
        a=0
        if T[i]=="A":
            a=1
        ta[i+1]=ta[i]+a
        
    def f(a1,b1,a2,b2):
        a1%=3
        a2=(a2%3)+3
        b1%=3
        b2=(b2%3)+3
        
        da=a2-a1
        db=b2-b1
        
        return not((da-db)%3)
    
    def calc(a,b,c,d):
        a1=sa[b]-sa[a-1]
        b1=(b-a+1)-a1
        
        a2=ta[d]-ta[c-1]
        b2=(d-c+1)-a2
        
        return f(a1,b1,a2,b2)
    
    Q=I()
    for _ in range(Q):
        a,b,c,d=MI()
        
        
        # print(S[a-1:b])
        # print(T[c-1:d])
        if calc(a,b,c,d):
            print("YES")
        else:
            print("NO")
            
            
        
        

main()

