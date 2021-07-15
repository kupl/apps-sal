# def find_and(arr):
#     ans = arr[0] 
#     for i in range(1, len(arr)):
#         ans = ans&arr[i]
#     return ans
# def checkEvenOdd(arr, n):
#   for i in range(n) :
#       if arr[i] % 2 == 0:
#           print("EVEN")
#           return
#   print("ODD")
# t = int(input())
# for _ in range(t):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     Q = int(input())
#     Nlst = []
#     for _ in range(Q):
#         L, R = map(int, input().strip().split())
#         z = checkEvenOdd(lst[L-1:R], len(lst[L-1:R]))
for _ in range(int(input())):
 n=int(input())
 lis=list(map(int,input().split()))
 q=int(input())
 s=''
 for i in range(n):
  if (lis[i]&1)==0:
   s+='0'
  else:
   s+='1'
 for _ in range(q):
  x=list(map(int,input().split()))
  l=x[0]
  r=x[1]
  temp='1'*((r+1)-l)
  if temp==s[l-1:r]:
   print("ODD")
  else:
   print("EVEN")
