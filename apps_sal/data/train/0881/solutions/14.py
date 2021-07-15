import sys

def iinput():   return int(sys.stdin.readline().strip())
#def rinput():   return map(int, sys.stdin.readline().strip().split()) 
def get_list(): return list(map(int, sys.stdin.readline().strip().split())) 


for _ in range(iinput()):
 n=iinput()
 c=0
 t=get_list()
 l=[1]*n
 for i in range(1,n):
  if(t[i-1]<=t[i]):
   l[i]+=l[i-1]
 #print(l)
 print(sum(l))

