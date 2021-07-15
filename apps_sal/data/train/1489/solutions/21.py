n,k=input().split()
k=int(k)
res = [x for x in str(n)]
i=0
while(k>0 and i<len(res)):
    if(res[i]!="9"):
        res[i]="9"
        k=k-1
        i=i+1
    else:
        i=i+1
st=""
x=st.join(res)
print(x)
        
    

