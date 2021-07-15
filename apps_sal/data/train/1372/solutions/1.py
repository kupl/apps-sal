# cook your dish here
for _ in range(int(input())):
 a,b,c,d=list(map(int,input().split()))
 p=(a*a)+(b*b)
 q=(c*c)+(d*d)
 if p<q:
  print("A IS CLOSER")
 else:
  print("B IS CLOSER")

