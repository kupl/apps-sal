n = int(input())
c = 0
son = sum(list(map(int, input().split()))) / 4
for i in range(n-1):
    others = sum(list(map(int, input().split()))) / 4
    if son >= others:
        c += 1
print(n-c)
