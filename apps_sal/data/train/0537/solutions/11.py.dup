# cook your dish here
N, K = map(int, input().split())
x = list(map(int, input().split()))[:N]
count = []
for i in range(len(x)):
    for j in range(i, len(x)):
        if abs(x[i] - x[j]) >= K:
            count.append(1)
print(len(count))
