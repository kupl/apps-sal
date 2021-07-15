# cook your dish here
n = int(input())
s = 0
for i in range(n):
 lst = list(map(int,input().split()))
 if sum(lst)>=2:
  s += 1
print(s)
