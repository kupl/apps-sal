(n, k) = input().split()
total = 0
for i in range(0, int(n)):
    t = int(input())
    if t % int(k) == 0:
        total += 1
print(total)
