n,k = map(int,input().split())
count = 0
for i in range(n):
    t = int(input())
    if t % k == 0:
        count += 1
print(count)
