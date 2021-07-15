for _ in range(int(input())):
 n,m=map(int,input().split())
 lim=n*m+1
 k=lim-1
 lst=[int(num) for num in range(1,lim)]
 lst2=[]
 for val in range(1,m+1):
  for val2 in range(n):
   lst2.append(val+(m*(val2)))
 for val_k in range(k):
  lst_k=[]
  for index in range(0,lim-1,val_k+1):
   lst_k.append(lst[index])
   lst_k.append(lst2[index])
  print(len(set(lst_k)),end=" ")
 print()
