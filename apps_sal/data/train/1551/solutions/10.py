# cook your dish here
t=int(input())
for _ in range(t):
 s=input()[:100]
 s.lower()
 k=s.split()
 if('not' in k):
  print("Real Fancy")
 else:
  print("regularly fancy")

