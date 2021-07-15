T = int(input())
ans = []

for _ in range(T):
 N = int(input())
 P = [int(i) for i in input().split()]

 m = min(P)
 ans.append((sum(P)-m)*m)

for i in ans:
 print(i)


