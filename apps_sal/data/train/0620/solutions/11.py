import sys

def _int():
 return int(sys.stdin.readline())

def _ints():
 return list(map(int, sys.stdin.readline().split()))

def _intarr():
 return list(map(int, sys.stdin.readline().split()))

def _str():
 return sys.stdin.readline()

def _strarr():
 return sys.stdin.readline().split()

t = _int()

ans = []

for _ in range(t):
 n, m = _ints()
 arr = _intarr()
 
 
 # start index of current calculation
 start = -1
 # end index of current calculation
 # used for edge cases
 end = -1
 # index of previous bigger than m
 # used for calculating start for next
 index = -1
 ans = 0
 for i in range(n):
  if start == -1:
   start = i
   if arr[i] > m:
    index = i
  else:
   if arr[i] > m:
    if index == -1:
     index = i
    elif arr[index] != arr[i]:
     end = i
     # calculate string length
     ans = max(ans, end-start)
     #print("{} {} {}".format(start, end, ans))
     # start new calculation with next element
     # of previos bigger than m
     start = index+1
    # previous bigger than m
    index = i
 if end != n-1:
  end = n
  ans = max(ans, end-start)
  #print("{} {} {}".format(start, end, ans))
 
 print(ans)

