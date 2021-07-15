from sys import stdin,stdout
def main():
    mod=10**9+7
    n=int(stdin.readline())
    neg=[0]*(500002)
    pos=[0]*(500002)
    counter=0
    mn=1000000
    mx=-1000000
    larr=[]
    rarr=[]
    for i in range(n):
        l,r=map(int,stdin.readline().split())
        if l<0:
            counter=1
            neg[abs(l)]+=1
        else:
            pos[l]+=1
        if r<0:
            neg[abs(r)-1]-=1
        else:
            pos[abs(r)+1]-=1
    ans=0
    for i in range(10**5,0,-1):
        neg[i]+=neg[i+1]
        ans=(ans+neg[i])%mod
    neg[0]=neg[0]+neg[1]
    pos[0]=neg[0]+pos[0]
    ans=(ans+pos[0])%mod
    for i in range(1,10**5+2):
        pos[i]=pos[i]+pos[i-1]
        ans=(ans+pos[i])%mod
    #print(neg[0:5])
    #print(pos[0:5])
    print(ans)
   
main()
