def checker(lst):
 le = len(lst)
 nlst = [0]*le
 for i in range(le):
  nlst[lst[i]-1] = i+1
  

 if nlst == lst:
  print("ambiguous")
 else:
  print("not ambiguous")


def __starting_point():
 while True:
  t = int(input())
  if t == 0:
   return
  else:
   arr = [int(i) for i in input().split()]
   checker(arr)

__starting_point()
