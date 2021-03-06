def abs(x):
    if x < 0:
        return -x
    else:
        return x


precalculated = {}
N = int(input())
tmp = input()
while tmp[-1] == ' ':
    tmp = tmp[:-1]
values = list(map(int, tmp.split(' ')))
total = 0
saved_sum = sum(values)
saved_length = len(values) - 1
for val in values:
    if val in precalculated:
        precalculated[val][1] += 1
    else:
        precalculated[val] = [0, 1]
        for val1 in values:
            precalculated[val][0] += abs(val - val1)
for pre in precalculated:
    total += precalculated[pre][0] * precalculated[pre][1]
print(total // 2)
