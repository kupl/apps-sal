for _ in range(int(input())):
 a = input()
 if len(a) == 1:
  print(0)
  continue
 comp = 0
 cont = 1
 ans = 0
 for i in range(1,len(a)):
  if a[i] == a[comp]:
   cont += 1
   if i == len(a) - 1:
    ans += (cont*(cont-1))//2
  else:
   ans += (cont*(cont-1))//2
   if comp != 0 and a[comp-1] == a[i]:
    ans += 1
   comp = i
   cont = 1
 print(ans)
