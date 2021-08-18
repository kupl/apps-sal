N, K = map(int, input().split(" "))
inputs = list(map(int, input().split(" ")))
inputs.sort()
data = [[inputs[0], 1]]
total = 0
previous = [inputs[0], 0]
for n in range(1, N):
    if inputs[n] == previous[0]:
        total += previous[1]
        data[0][1] += 1
    else:
        flag = True
        for point in data:
            if inputs[n] - point[0] >= K:
                total += point[1]
                previous = [inputs[n], point[1]]
                flag = False
                break
        data = [[inputs[n], data[0][1] + 1]] + data
        if flag:
            previous = [inputs[n], 0]
print(total)
