N = int(input())
for _ in range(N):
    (a, b) = list(map(int, input().split(' ')))
    distance = 0
    while a != b:
        distance += 1
        (a, b) = (a, b / 2) if a < b else (a / 2, b)
    print(distance)
