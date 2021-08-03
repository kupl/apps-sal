N = int(input())
station = [0] * (N + 1)
for i in range(N):
    amount, distance = list(map(int, input().split()))
    station[i] = (amount, distance)

for c in range(N):
    i = c
    p = station[i][0]
    while i < c + N and p >= station[i % N][1]:
        p += station[(i + 1) % N][0] - station[i % N][1]
        i += 1
    if i == c + N:
        break
    c = i + 1
print(c)
