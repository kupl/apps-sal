# cook your dish here
from collections import defaultdict

def preCompute(arr, n, K):
 nonlocal maxDistance
 arr = list(enumerate(arr))
 arr.sort(key = lambda x: -x[1])
 # print(arr)
 maxDistance[arr[0][0]] = arr[0][1] + K
 for i in range(1, n):
  if arr[i-1][1] - arr[i][1] <= K:
   maxDistance[arr[i][0]] = maxDistance[arr[i-1][0]]
  else:
   maxDistance[arr[i][0]] = arr[i][1] + K

def answer(x, y):
 # print(maxDistance)
 if maxDistance[x-1] == maxDistance[y-1]:
  return "Yes"
 return "No"


maxDistance = defaultdict(int)
(n, k, p) = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
preCompute(arr, n, k)
for _ in range(p):
 (x, y) = map(int, input().strip().split())
 print(answer(x, y))
