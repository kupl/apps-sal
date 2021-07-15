for i in range(int(input())):
 li=list(map(int,input().split()))
 t=abs(sum(li)-max(li))
 if(t>=max(li)-1):
  print("Yes")
 else:
  print("No")

