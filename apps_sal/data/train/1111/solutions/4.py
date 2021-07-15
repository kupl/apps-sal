# cook your dish 
for _ in range(int(input())):
 x = int(input())
 arr = list(map(int,input().split()))
 count = 0
 if (x ==1):
  print("0")
 else:
  for i in range(x-1):
   if ((arr[i] + arr[-1]) % 2==1 ):
    count +=1
  print(count)

