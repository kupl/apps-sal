# cook your dish here
t = int(input())
for _ in range(t):
 n, m = map(int, input().strip().split())
 arr = list(map(int, input().strip().split()))
 
 not_done = [i for i in range(1, n+1) if i not in arr]
 chef = [not_done[i] for i in range(len(not_done)) if i % 2 == 0]
 assis = [not_done[i] for i in range(len(not_done)) if i % 2 == 1]
 print(*chef)
 print(*assis)
