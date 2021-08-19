# cook your dish here
N, K = map(int, input().split(" "))
inputs = list(map(int, input().split(" ")))
inputs.sort()
total = 0
previous = [None, None]
for n in range(1, N):
    if inputs[n] == previous[0]:
        total += previous[1]
        continue
    previous = [None, None]
    for i in range(n - 1, -1, -1):
        tmp = inputs[n] - inputs[i]
        if tmp < 0:
            tmp = -tmp
        if tmp >= K:
            total += i + 1
            previous[1] = i + 1
            previous[0] = inputs[n]
            break
    if previous[0] is None:
        previous[0] = inputs[n]
        previous[1] = 0
print(total)
