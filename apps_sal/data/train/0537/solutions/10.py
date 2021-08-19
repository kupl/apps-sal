# cook your dish here
N, K = map(int, input().split(" "))
inputs = list(map(int, input().split(" ")))
inputs.sort()
total = 0
for n in range(N):
    for i in range(n - 1, -1, -1):
        tmp = inputs[n] - inputs[i]
        if tmp < 0:
            tmp = -tmp
        if tmp >= K:
            total += i + 1
            break
print(total)
