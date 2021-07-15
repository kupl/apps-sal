import sys

ngs = "0124679"
def judge(p):
 for i in ngs:
  if i in p:
   return False
 return p.count("3") <= p.count("5") <= p.count("8")

n = int(input())
res = 0
for i in range(n):
 p = sys.stdin.readline().split()[-1].strip()
 if judge(p): res += 1
print(res)

