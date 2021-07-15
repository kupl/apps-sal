# cook your dish here
T = int(input())
for j in range(T):
 n = int(input())
 a = list(map(int, input().split()))
 a.sort(reverse=True)
 print(sum(a[::2]))
