for _ in range(int(input())):
 n = int(input())
 arr = list(map(int,input().split()))
 A = set(arr)
 B = set(arr[i-1] for i in A)
 if A == B:
  print("Poor Chef")
 else:
  print("Truly Happy")
