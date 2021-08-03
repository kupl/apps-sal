N = int(input())
r = range(1, N + 1)
count = 0
for i in r:
    for j in r:
        if i * j >= N:
            break
        count += 1
print(count)
