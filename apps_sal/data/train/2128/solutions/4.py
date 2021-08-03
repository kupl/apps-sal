import fileinput
for line in fileinput.input():
    x = [int(i) for i in line.split()]

rightCows = 0
total = 0

for i in range(0, len(x)):
    if x[i]:
        rightCows += 1
    else:
        total += rightCows

print(total)
