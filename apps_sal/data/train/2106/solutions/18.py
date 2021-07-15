from sys import stdin
from collections import deque
import heapq
n = int(stdin.readline())

piles = []

for x in range(n):
    a = [int(x) for x in stdin.readline().split()][1:]
    piles.append(a)

cielTotal = 0
jiroTotal = 0

mids = []

for x in piles:
    cielTotal += sum(x[:len(x)//2])
    jiroTotal += sum(x[len(x)//2+len(x)%2:])
    #print(x)
    #print(cielTotal,jiroTotal)
    if len(x)%2 == 1:
        mids.append(x[len(x)//2])

mids.sort(reverse=True)

turn = True
for x in mids:
    if turn:
        cielTotal += x
    else:
        jiroTotal += x
    turn = not turn
print(cielTotal,jiroTotal)

    

