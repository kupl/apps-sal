import re
import sys


def isCirlePossible(juices, distances):
    if juices == [] or distances == []:
        return -1
    total_juice_consumed = 0
    juice_consumed = 0
    start = 0
    for i in range(0, len(juices)):
        diff = juices[i] - distances[i]
        if juice_consumed >= 0:
            juice_consumed += diff
        else:
            juice_consumed = diff
            start = i
        total_juice_consumed += diff
    return start


juices = []
distances = []
numLines = int(input())
for each in range(0, numLines):
    line = input()
    result = [int(x) for x in re.findall('\d+', line)]
    if len(result) == 2:
        juices.append(result[0])
        distances.append(result[1])

print(isCirlePossible(juices, distances))
return
