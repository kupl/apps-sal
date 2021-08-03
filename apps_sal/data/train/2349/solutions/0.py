import sys
from math import log

k = float(sys.stdin.readline())
answer = int(log(2.0, 2.0 / k))
print(2 * answer)

m = 2 ** (1.0 / answer)
# m = 2.0/k
thesum = 0
for i in range(answer):
    thesum += m**i
# print [m**i/thesum for i in xrange(answer)]
loaves = [1]


def maxIndex(list):
    max = -1
    mi = -1
    for i, x in enumerate(list):
        if x > max:
            max = x
            mi = i
    return mi


desired = [m**i / thesum for i in range(answer)]
desired.reverse()
# print desired
cuts = []
while len(desired) > 1:
    cuts.append(desired[-1])
    lastsum = desired[-1] + desired[-2]
    del desired[-2:]
    desired[0:0] = [lastsum]

# print cuts

while cuts:
    length = cuts.pop()
    i = maxIndex(loaves)
    print(i, length)
    loaves[i] -= length
    loaves.append(length)
    # print loaves

# print loaves
for i in range(answer):
    i = maxIndex(loaves[:answer])
    x = loaves[i] / 2.0
    print(i, x)
    loaves.append(x)
    loaves[i] -= x
# print loaves
