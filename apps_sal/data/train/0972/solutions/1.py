N,K=map(int,input().split())
l=[]
i=0
while i<N:
    i+=1
    l.append(int(input()))
l.sort()
m='n'
for i in range(N-K+1):
    if m=='n' or l[i+K-1]-l[i]<m:
        m=l[i+K-1]-l[i]
print(m)
