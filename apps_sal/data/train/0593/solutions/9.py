import string
check=string.ascii_lowercase
for _ in range(int(input())):
 price=0
 l=list(map(int,input().strip().split()))
 s=str(input())
 s=set(s)
 for i in range(0, len(check)):
  if check[i] not in s:
   price += l[i]
 print(price)
