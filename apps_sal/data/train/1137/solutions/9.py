# cook your dish here
for _ in range(int(input())):
 n = int(input())
 t = False
 arr = list(map(int, input().split()))
 if(arr.count(1000)==2):
  print("Accepted")
  continue
 s = set(arr)
 for i in s:
  if i<1000 and 2000-i in s:
   t = True
   break
 print("Accepted" if t else "Rejected")
