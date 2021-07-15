input_1 = int(input())

for i in range(input_1):
 input_2 = int(input())
 arr = list(map(int, input().split()))
 count = 1
 mini = arr[0]
 if input_2 ==1:
  print(count)
 else:
  for j in range(1,input_2):
   if arr[j] <= mini:
    mini = arr[j]
    count = count +1
  print(count)
