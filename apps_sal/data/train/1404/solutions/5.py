t=input()
t=int(t)
while t>0:
 inp=input()
 values=inp.split()
 
 k=input()
 k=int(k)
 
 
 lst1 = [int(values[0]), int(values[1]), int(values[2])]
 lst = sorted(lst1)
 
 
  
 
 if lst[0]>=k:
  num=((k-1)*3)+1
  print(num)
 elif lst[1]>=k:
  num= (lst[0]*3)+((k-lst[0]-1)*2)+1
  print(num)
 elif lst[2]>=k:
  num= (lst[0]*3)+((lst[1]-lst[0])*2)+(k-lst[1])
  print(num)
 
 
 t=t-1
