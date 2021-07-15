'''
Created on 2020/09/03

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N=int(pin())
  a=list(map(int,pin().split()))
  s=0
  for i in a:
    s=s^i 
  ansl=[]
  for j in a:
    ansl.append(str(s^j))
  ans=" ".join(ansl)
  print(ans)
  return 
main()
