n = int(input())
point = [int(item) for item in input().split(' ')]
point.sort()
a = (point[n - 1] - point[0]) * (point[n + n - 1] - point[n])
b = (point[-1] - point[0]) * min(point[n - 1 + i] - point[i] for i in range(n))

print(min(a, b))

