size = int(input())
array = []

for x in range(size):
    array.append(int(input()))

diff = 0

for i in range(size):
    for j in range(i + 1, size):
        if array[i] % array[j] > diff:
            diff = array[i] % array[j]

print(diff)
