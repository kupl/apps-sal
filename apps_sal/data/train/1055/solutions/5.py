(n, m) = map(int, input().split())
slices = [int(x) for x in input().split()]
slices.sort()
array = [0] * (slices[-1] + 1)
array[0] = 1
for i in range(1, len(array)):
    array[i] = array[i - 1] + i
total = 0
slices = slices[::-1]
value = 0
for i in range(len(slices)):
    if slices[i] <= m:
        total += array[slices[i]]
        m -= slices[i]
        continue
    if m < slices[i]:
        total += array[m]
        m = 0
        value = len(slices) - i - 1
        break
total += value
print(total)
