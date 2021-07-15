for i in range(int(input())):
 n=int(input())
 a=[]
 p1=p2=0
 for j in range(n):
  s=input()
  a.append([s[:n//2].count('1'),s[n//2:].count('1')])
  p1+=a[j][0]
  p2+=a[j][1]
 m=abs(p1-p2)
 tp2=p2
 tp1=p1
 for j in range(n):
  tp1-=a[j][0]
  tp1+=a[j][1]
  tp2-=a[j][1]
  tp2+=a[j][0]
  if m>abs(tp1-tp2):
   m=abs(tp1-tp2)
  tp1=p1
  tp2=p2
 print(m)

