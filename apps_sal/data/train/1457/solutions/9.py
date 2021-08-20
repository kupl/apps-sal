(n, k) = input().split()
count = 0
for i in range(0, int(n)):
    x = int(input())
    if x % int(k) == 0:
        count += 1
    else:
        continue
print(count)
