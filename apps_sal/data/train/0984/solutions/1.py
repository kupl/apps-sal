for t in range(int(input())):
 n = int(input())
 numberlist = list(map(int,input().split()))
 count = 0
 for i in range(len(numberlist)-1):
  for j in range(i+1,len(numberlist)):
   if numberlist[i]%2 == 0:
    if numberlist[j]%2==1 :
     count+=1
 print(count)
