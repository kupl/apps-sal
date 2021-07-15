
t = int(input())
while t:
 t -= 1
 n = int(input())
 arr = list(map(int, input().split()))
 sumi = sum(arr)
 prev = 1
 for i in range(n):
  arr[i] = min(arr[i], prev)
  prev = arr[i] + 1
 prev = 1
 for i in range(n - 1, -1, -1):
  arr[i] = min(arr[i], prev)
  prev = arr[i] + 1
 temp = 0
 for i in range(n):
  temp = max(temp, arr[i])
 print(sumi -( temp*temp))



