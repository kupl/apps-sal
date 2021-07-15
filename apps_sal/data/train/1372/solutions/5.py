n=int(input())
for _ in range(n):
 arr=list(map(int,input().split()))
 if (abs(arr[0])+abs(arr[1]))>(abs(arr[2])+abs(arr[3])):
  print("B IS CLOSER")
 else:
  print("A IS CLOSER")

