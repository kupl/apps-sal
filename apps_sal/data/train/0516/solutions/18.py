# cook your dish here
t=int(eval(input()))
for i in range(t):
    inp = list(map(int,input().split()))
    n=inp[0]
    k=inp[1]
    inp = list(map(int,input().split()))
    before=[]
    after=[]
    ans=0
    for p in range(len(inp)):
        bef_count=0
        af_count=0
        for q in range(len(inp)):
            if(q>p and inp[q]<inp[p]):
                af_count+=1
            elif(q<p and inp[q]<inp[p]):
                bef_count+=1
        ans+=af_count*(k*(k+1))//2
        ans+=bef_count*(k*(k-1))//2
    print(ans)
