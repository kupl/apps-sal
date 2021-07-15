# cook your dish here
t=int(input())
for _ in range(t):
 n,k=map(int,input().split())
 l=input()
 count=0
 i=0
 j=0
 while i<n and j<n:
  if l[i]=="M":
   if l[j]=="I":
    if i<j:
     sij=l[i:j].count(":")
    else:
     sij=l[j:i].count(":")
    p=k+1-abs(i-j)-sij
    if p>0:
     count+=1
     i+=1
     j+=1
    else:
     if i<j:
      i+=1
     else:
      j+=1
   elif l[j]=="X":
    j+=1
    i=j
   else:
    j+=1
  elif l[i]=="X":
   i+=1
   j=i
  else:
   i+=1
 print(count)
