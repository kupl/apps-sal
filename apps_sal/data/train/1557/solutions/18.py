# cook your dish here
def cricketbetterthana(s,b):
 if s.count('1')!=b.count('1'):
  return False
 return True
for _ in range(int(input())):
 n=int(input())
 s=list(input())
 b=list(input())
 if cricketbetterthana(s,b):
  print("YES")
 else:
  print("NO")

