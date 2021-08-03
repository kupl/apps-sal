n = input()
l = list(map(int, input().split()))
x = 0
y = 0
for i in l:
    x += i // 2
    y += (i + 1) // 2
    x, y = y, x
print(min(x, y))
