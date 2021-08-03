# cook your dish here
n = int(input())
l = list(map(int, input().split()))
k = int(input())
t = list()
for i in range(k + 1):
    t.append(sum(l[0:i]) + sum(l[n - (k - i):n]))
print(max(t))
