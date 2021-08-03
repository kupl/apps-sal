z, x, y = map(int, input().split())
n = int(input())
tot = 0
l = list(map(int, input().split()))
for i in l:
    if(i < y and i > x):
        tot += 1
print(tot)
