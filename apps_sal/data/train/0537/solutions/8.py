(N, K) = map(int, input().split(' '))
inputs = list(map(int, input().split(' ')))
inputs.sort()
data = [[None, 0]]
total = 0
previous = [None, None]
for n in range(N):
    if inputs[n] == previous[0]:
        total += previous[1]
        data[0][1] += 1
    else:
        previous = [None, None]
        data = [[inputs[n], data[0][1] + 1]] + data
        for point in data[1:-1]:
            if inputs[n] - point[0] >= K:
                total += point[1]
                previous = [inputs[n], point[1]]
                break
        if previous == [None, None]:
            previous = [inputs[n], 0]
print(total)
