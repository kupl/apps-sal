t = int(input())
for i in range(t):
 N = int(input())
 An = list(map(int, input().split(" ")))
 cumsum = []
 cumsum.append(An[0])
 for j in range(N-1):
  cumsum.append(cumsum[j] + An[j+1])
 days = 0
 k = 0
 while(k < N-1):
  days += 1
  k = k + cumsum[k]
 print(days)

