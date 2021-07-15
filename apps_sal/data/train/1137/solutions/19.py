def main():
 for _ in range(int(input())):
  n=int(input())
  a=list(map(int,input().split()))
  flag=False
  s=set(a)
  if(a.count(1000)>=2):
   flag=True
  for i in a:
   if(2000-i in s and i!=1000):
    flag=True
    break
  print("Accepted" if(flag) else "Rejected")
main()
