# cook your dish here
for _ in range(int(input())):
 n = int(input())
 l1 = list(map(int, input().split()))
 ans = [l1[i - 1] - l1[i] for i in range(1, len(l1))]
 print(min(ans))
