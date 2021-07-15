for _ in range(int(input())):
 st=input().replace("=","")
 if not len(st):print(1)
 else:
  cu=mx=1
  for j in range(1,len(st)):
   if st[j]==st[j-1]:cu+=1
   else:mx=max(mx,cu);cu=1
  print(max(mx+1,cu+1))

