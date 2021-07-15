# cook your dish here
from sys import stdin, stdout
import math


def lower_bound(arr, ele):
 low = 0
 high = len(arr)-1
 while low <= high:
  mid = (low+high)//2
  if arr[mid] == ele:
   return arr[mid]
  elif ele < arr[mid]:
   high = mid-1
  else:
   low = mid+1
 if high > len(arr)-1 or high < 0:
  return -1
 return arr[high]


def upper_bound(arr, ele):
 low = 0
 high = len(arr)-1
 while low <= high:
  mid = (low+high)//2
  if arr[mid] == ele:
   return arr[mid]
  elif ele < arr[mid]:
   high = mid-1
  else:
   low = mid+1
 if low > len(arr)-1 or low < 0:
  return -1
 return arr[low]


def main():
 n, n_x, n_y = list(map(int, stdin.readline().split()))
 contests = [None]*n
 for i in range(n):
  start, end = list(map(int, stdin.readline().split()))
  contests[i] = (start, end)
 V = [int(x) for x in stdin.readline().split()]
 W = [int(x) for x in stdin.readline().split()]
 V.sort()
 W.sort()
 ans = math.inf
 for (start, end) in contests:
  opv = lower_bound(V, start)
  opw = upper_bound(W, end)
  if opv == -1 or opw == -1:
   continue
  ans = min(ans, opw - opv + 1)
 print(ans)


def __starting_point():
 main()

__starting_point()
