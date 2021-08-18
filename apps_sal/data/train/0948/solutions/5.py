
x, y = list(map(int, input().split()))
pair = 0
for i in range(1, x + 1):
    pair += int(((i**2) + y)**0.5) - i
print(pair)
