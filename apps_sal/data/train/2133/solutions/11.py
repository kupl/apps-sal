n = int(input().strip())
classes = []
for _ in range(n):
    classes.append(int(input().strip()))
biggest = -1
for x in range(8):
    biggest = max(biggest, sum([x % 10 for x in classes]))
    classes = [x // 10 for x in classes]
print(biggest)
