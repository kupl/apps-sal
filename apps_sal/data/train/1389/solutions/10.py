import re
n = int(input())
line = ''
lines = []
for i in range(n):
    line = input()
    line = re.sub("[\\.,\\';:]+", '', line)
    line = re.sub('\\s+', ' ', line)
    lines.append(line.split()[::-1])
lines.reverse()
for i in range(n):
    for j in range(len(lines[i])):
        if j < len(lines[i]):
            print(lines[i][j], '', end='')
    print()
