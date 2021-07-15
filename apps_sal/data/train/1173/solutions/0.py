import itertools
from collections import defaultdict as dfd
def sumPairs(arr, n):
 s = 0
 for i in range(n-1,-1,-1): 
  s += i*arr[i]-(n-1-i)*arr[i]
 return s

def subarrayXor(arr, n, m):
 ans = 0
 xorArr =[0 for _ in range(n)]
 mp = dfd(list)
 xorArr[0] = arr[0]
 for i in range(1, n): 
  xorArr[i] = xorArr[i - 1] ^ arr[i]
 for i in range(n):
  mp[xorArr[i]].append(i)
 a = sorted(mp.items())
 #print(xorArr)
 #print(a)
 for i in a:
  diffs=0
  if(i[0]!=0):
   l = len(i[1])-1
   ans += sumPairs(i[1],len(i[1]))-((l*(l+1))//2)
   
  else:
   l = len(i[1])-1
   ans += sumPairs(i[1],len(i[1]))-((l*(l+1))//2)
   ans += sum(i[1])
 return ans

for _ in range(int(input())):
 n = int(input())
 arr = list(map(int,input().split()))
 print(subarrayXor(arr,len(arr),0))
