N = int(input())
print(2)
for n in range(2, N + 1):
    clicks = n * (n + 1)**2 - (n - 1)
    print(clicks)
