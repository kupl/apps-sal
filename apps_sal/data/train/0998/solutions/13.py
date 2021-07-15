n,k=list(map(int,input().strip().split()))
m1=dict()
m2=dict()
for _ in range(k):
 list1=input().split()
 a=list1[0]
 b=int(list1[1])
 c=int(list1[2])
 
 if a=="RowAdd":
  if b in m1:
   m1[b]+=c
  else:
   m1[b]=c
 else:
  if b in m2:
   m2[b]+=c
  else:
   m2[b]=c
max1=0
for val in m1:
 if m1[val]>max1:
  max1=m1[val]

max2=0
for val in m2:
 if m2[val]>max2:
  max2=m2[val]

print(max1+max2)
 
  

