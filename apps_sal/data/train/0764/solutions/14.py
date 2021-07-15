# cook your dish here
t=int(input())
def do():
 a=[d for d in input().split()]
 b=[e for e in input().split()]
 if len(set(a)&set(b))>=2:
  print('similar')
 else:
  print('dissimilar')
 return
for i in range(t):
 do()
 

