import sys
read = sys.stdin.readline


n = int(read())
balance = list(map(int, read().split(" ")))
n_operations = int(read())

minis = []
next_mini = 0
changed_before = [0] * (len(balance)+1)

for n_op in range(n_operations):
    operation = list(map(int, read().split(" ")))
    if operation[0] == 1:
        x = operation[1] - 1
        balance[x] = operation[2]
        changed_before[x] = next_mini
    elif operation[0] == 2:
        minis.append(operation[1])
        next_mini += 1

if len(minis) > 0:
    max_mini = minis[-1]
    for m in range(1, len(minis) + 1):
        max_mini = max(max_mini, minis[m * -1])
        minis[m * -1] = max_mini

    for x in range(len(balance)):
        cb = changed_before[x]
        if cb < next_mini:
            balance[x] = max(minis[cb], balance[x])
        balance[x] = str(balance[x])
else:
    for x in range(len(balance)):
        balance[x] = str(balance[x])

print(" ".join(balance))
