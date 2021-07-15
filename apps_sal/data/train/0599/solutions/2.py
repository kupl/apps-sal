# cook your dish here
def answer():
 m=max(w)
 count=[]
 c=0
 for i in w:
  if(i==m):
   count.append(c)
   c=-1
  c+=1

 if(c):
  count.append(c)

 first=(w[0]!=m)
 last=(w[-1]!=m)

 if(first and last):
  count[0]+=count[-1]
  count.pop()

 k=0 
 for i in count:
  if(i >= n//2):
   k+=i-n//2+1
 return k
 
   

for T in range(int(input())):
 n=int(input())
 w=list(map(int,input().split()))

 print(answer())

