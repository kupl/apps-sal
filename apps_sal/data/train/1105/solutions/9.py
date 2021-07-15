t=int(input(""))
for _ in range(t):
 n=int(input(""))
 l=list(map(int,input("").strip().split()))[:n]
 l.sort(reverse=True)
 b1=b2=0
 for i in l:
   if b1<b2:
    b1+=i
   else:
    b2+=i
 print(max(b1,b2))
