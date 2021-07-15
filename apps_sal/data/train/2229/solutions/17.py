#print('HARE KRISHNA')
t=input()
p=input()
block=[int(i)-1 for i in input().split()]
ind={}
for i in range(len(block)):
    ind[block[i]]=i 
def is_part_and_parcel(s1,s2,mid):
    n=len(s2)
    m=len(s1)
    i=0 
    c=0 
    j=0 
    while i<n and j<m:
        if ind[j]<mid:
            j+=1 
            continue 
        if s2[i]==s1[j]:
            i+=1
            j+=1 
            c+=1 
        else:
            j+=1 
    return c==n 
n=len(t)
m=len(p)
lo= 0 
hi=len(block)-1 
while lo<=hi:
    mi=(lo+hi)>>1 
    if is_part_and_parcel(t,p,mi):
        ans=mi 
        lo=mi+1 
    else:
        hi=mi-1 
print(ans)
