(a, b, c) = map(int, input().split())
n = int(input())
mass = list(map(int, input().split()))
mon = 0
for i in range(len(mass)):
    if b < mass[i] < c:
        mon += 1
print(mon)
