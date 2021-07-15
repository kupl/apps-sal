# cook your dish here
# cook your dish here
t=int(input(''))
for k in range (t):
 n=int(input(''))
 li=[]
 li1=[]
 li2=[]
 for i in range (n):
  p,q=input().split()
  p=int(p)
  q=int(q)
  li.append(p)
  li1.append(q)
 r=li[1]-li[0]
 #print(r)
 li2.append(r)
 for i in range (1,n-1):
  p=li[i+1]-li[i-1]
  li2.append(p)
 li2.append(li[n-1]-li[n-2])
 li2.sort()
 li1.sort()
 ans=0
 for i in range (n):
  ans=ans+li1[i]*li2[i]
  #print(li2[i])
 print(ans)
