for i in range(int(input())):
 n = int(input())
 arr = list(map(int, input().split()))
 arr.sort()
 for j in range(n-1, 0, -1):
  arr[j-1] = (arr[j] + arr[j-1])/2
 print(arr[0])
