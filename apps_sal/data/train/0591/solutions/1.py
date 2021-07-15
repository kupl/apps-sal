# cook your dish here
def s(n):
 sn=str(n)
 r=0
 for i in sn:
  r+=int(i)
 return r
  
for _ in range(int(input())):
 n=int(input())
 print(str(n)+str((10-s(n))%10))
