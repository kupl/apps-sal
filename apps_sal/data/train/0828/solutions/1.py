for i in range(int(input())):
  x=int(input())
  y=input().split()
  if '0' in y:
    print(100*(x-y.index('0'))+y.count('0')*1000)
  else:
    print(0)  
