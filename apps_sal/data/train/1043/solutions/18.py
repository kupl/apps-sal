# cook your dish here
for _ in range(int(input())):
 n,k = map(int,input().split())
 word = list(input().split())
 li = []
 for x in range(k):
  l = list(input().split())
  li += l
 for x in word:
  if x in li:
   print("YES",end=" ")
  else:
   print("NO",end=" ")
 print()
