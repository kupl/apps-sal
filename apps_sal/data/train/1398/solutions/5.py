from sys import stdin as sin
def aint():return int(input())
def amap():return map(int,sin.readline().split())
def alist():return list(map(int,sin.readline().split()))
def astr():return input()



for _ in range(int(input())):
 s=input()
 f=[0]*26
 m=0
 for i in range(len(s)):
  if not f[ord(s[i])-97]:
   m+=1
   f[ord(s[i])-97]=1
   
 print(m)
