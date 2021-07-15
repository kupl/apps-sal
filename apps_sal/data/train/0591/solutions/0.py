for _ in range(int(input())):
 N = input()
 num = list(N)
 s=0
 for n in num:
  if n.isnumeric():
   s+=int(n)
 #print(s)
 x=(10-s%10)%10
 print(int(N)*10+int(x))
