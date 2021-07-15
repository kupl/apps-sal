tc = int(input())
for itercnt in range(tc):
 str1 = input()
 str2 = input()
 cnt = 0
 for x in str2:
  for y in str1:
   if (x == y): 
    cnt+=1
    break
 print(cnt)
