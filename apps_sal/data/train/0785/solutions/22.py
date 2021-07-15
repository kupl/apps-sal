for _ in range(int(input())):
 a=int(input())
 s=1
 s1=a
 p=a-s
 d=1
 b=[]
 for i in range(2,100):
  if p<=0:
   d=i-2
   break
  else:
   b.append(p)
   s+=pow(2,i-1)
   a+=s1
   p=a-s
 print(d,b.index(max(b))+1)
