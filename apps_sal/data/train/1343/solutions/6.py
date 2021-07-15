for _ in range(int(input())):
 s = input()
 s = list(s)
 s1 = s
 f = 0
 l = len(s)
 if l >= 2:
  for i in range(l):
   if l % 2 == 0:
    ln = l
    tp1 = s1[:(ln//2)]
    tp2 = s1[(ln//2):]
    if str(tp1) == str(tp2):
     f = 1
     break
   else:    
    if i == 0:
     tmp = s1[i+1:]
     ln = l - 1
     tp1 = tmp[:(ln//2)]
     tp2 = tmp[(ln//2):]
     if str(tp1) == str(tp2):
      f = 1
      break
    else:
     tmp = s1[:i]
     tmp2 = s1[i+1:]
     temp = tmp + tmp2
     ln = l - 1
     tp1 = temp[:(ln//2)]
     tp2 = temp[(ln//2):]
     if str(tp1) == str(tp2):
      f = 1
      break
  if f == 1:
   print("YES")
  else:
   print("NO")
 elif l == 1:
  print("NO")
  

