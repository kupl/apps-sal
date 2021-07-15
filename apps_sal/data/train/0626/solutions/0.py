t=int(input())
def reversebinary(bits,n):
    bStr=''
    for i in range(bits):
        if n>0:
            bStr=bStr+str(n%2)
        else:
            bStr=bStr+'0'
        n=n>>1
    return int(bStr,2)
        
for i in range(t):
    k,msg=input().split()
    k=int(k)
    newmsg=[]
    for j in msg:
        newmsg.append(j)
    for j in range(len(msg)):
        newmsg[reversebinary(k,j)]=msg[j]
    print(''.join(newmsg))
        
    

