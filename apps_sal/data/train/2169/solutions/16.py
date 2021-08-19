line = input()
line = line.split()
line = list([int(x) for x in line])
n = line[0]
p = line[1]
k = line[2]
inputs = input()
inputs = inputs.split()
inputs = list([int(x) for x in inputs])
dict = {}
counter = 0
for i in range(n):
    exped = ((inputs[i] ** 2) ** 2 - k * inputs[i]) % p
    if dict.get(exped, None) is None:
        dict[exped] = 0
    counter = counter + dict[exped]
    dict[exped] = dict[exped] + 1
print(counter)
