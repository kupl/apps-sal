n,q=map(int,input().split())
dr={}
dc={}
for i in range(1,n+1):
 dr[i]=0
 dc[i]=0
mer=0
mec=0
for i in range(q):
 s,j,k=input().split()
 j=int(j)
 k=int(k)
 if s=="RowAdd":
  dr[j]+=k
  if dr[j]>mer:
   mer=dr[j]
 else:
  dc[j]+=k
  if mec<dc[j]:
   mec=dc[j]
# m=max(list(dr.values()))+max(list(dc.values()))

# for i in range(n):
#     for j in range(n):
#         ar[i][j]=dr[i+1]+dc[j+1]
#         if ar[i][j]>m:
#             m=ar[i][j]

print(mer+mec)
