T = int(input())
ans = []

for _ in range(T):
 N = int(input())
 A = [int(i) for i in input().split()]

 A.sort(reverse=True)
 count = 0
 for i in range(0,N,2):
  count += A[i]
 ans.append(count)

for i in ans:
 print(i)

