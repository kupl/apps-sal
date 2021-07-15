t = int(input())
for _ in range(t):
     n = int(input())
     a = [int(i) for i in input().split()]
     ans = []
     for i in a:
          if i not in ans:
               ans.append(i)
     print(*ans)
