T=int(input())
while T<1 or T>10:
 T=int(input())
for i in range(T):
 n = int(input())
 a =list(map(int, input().strip().split(" ")))
 sum = 0
 k = 0
 for j in a:
  sum = sum + j
  k = k + 1
 avg = sum / k
 if avg % 1 == 0:
  print('Yes')
 else:
  print('No')

