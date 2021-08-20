list = []
x = int(input())
output = []
for i in range(x):
    count = 0
    val = int(input())
    line = input()
    z = line.split()
    z = [int(y) for y in z]
    for j in z:
        if j == 0:
            count += 1
    output.append(count)
for i in output:
    print(i)
