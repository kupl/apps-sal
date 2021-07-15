for _ in range(int(input())):
 n,k = [int(x) for x in input().split()]
 lst = [int(x) for x in input().split()]
 lst.sort(reverse=True)
 el = lst[k-1]
 count = 0
 for i in lst:
  if i<el:
   break
  else:
   count = count + 1
 print(count)

