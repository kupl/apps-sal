
d=input().split()
money=int(d[1])
price_of_chocolates=sorted(list(map(int,input().split())))
price=None
n=0
for f in price_of_chocolates:
 if price is None and f<=money:
  price=f
  n+=1
 elif price+f<=money:
  price+=f
  n+=1
 else:
  break
print(n)
