# cook your dish here
def pairs(arr):
 x=0
 pairs=0
 for i in range(len(arr)):
  if arr[i]%2==0:
   x=x+1
  else:
   pairs=pairs+x
 return pairs
test_cases=int(input())
for i in range(test_cases):
 x=int(input())
 arr=list(map(int,input().rstrip().split()))
 print(pairs(arr))
