# cook your dish here
T = int(input())
for j in range(T):
 ran = list(map(int, input().rstrip().split()))
 count=0
 for i in range(ran[0],ran[1]+1):
  if(i%10==2 or i%10 == 3 or i%10 == 9):
   count+=1
 print(count)
