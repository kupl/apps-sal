def bsearch(arr,num,start,end):
    mid=int((start+end)/2)
    if start>end:
        return (start,0)
    if arr[mid]==num:
        return (mid,1)
    elif arr[mid]<num:
        return bsearch(arr,num,mid+1,end)
    else:
        return bsearch(arr,num,start,mid-1)
t=int(input())
A=[]
B=[]
N=[]#next undestroyed beacon
NUM=[]#number of destroyed beacon if current veacon activated

abp=[]
for i in range(0,t):
    ab=input().split(' ')
    a,b=int(ab[0]),int(ab[1])
    abp.append((a,b))
abp_S=sorted(abp,key = lambda bk:bk[0])
for i in range(0,len(abp_S)):
    a,b=abp_S[i]
    A.append(a)
    B.append(b)
    pos=bsearch(A,a-b,0,len(A)-1) 
    if pos[0]==0:
        N.append(pos[0]-1)
        NUM.append(i)
    else:
        N.append(pos[0]-1)
        NUM.append((i-pos[0])+NUM[pos[0]-1])
damages=[]
for i in range(0,len(A)):
    damages.append((len(A)-(i+1))+NUM[i])
print(min(damages))



