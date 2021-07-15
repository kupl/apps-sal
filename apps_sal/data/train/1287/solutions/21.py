t=int(input())
for i in range(t):
 st=input()
 bi=list(map(lambda c:str(int(c.lower() in ['a','i','e','o','u'])),st))
 print(int("".join(bi),2)%(10**9+7))
