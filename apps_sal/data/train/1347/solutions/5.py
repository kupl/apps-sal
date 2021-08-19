import numpy
inp = list(map(int, input().split()))
n = inp[0]
m = inp[1]
inp1 = list(map(int, input().split()))
arrayf = []
arrayp = []
arrays = []
arrayfBest = []
arraypBest = []
arraysBest = []
countBest = 0
countOther = 0
for i in range(m):
    inp3 = list(input().split())
    if int(inp3[0]) in inp1:
        arrayfBest.append(int(inp3[0]))
        arraypBest.append(int(inp3[1]))
        arraysBest.append(inp3[2])
        countBest = countBest + 1
    else:
        arrayf.append(int(inp3[0]))
        arrayp.append(int(inp3[1]))
        arrays.append(inp3[2])
        countOther = countOther + 1
sortedString = [x for (y, x) in sorted(zip(arraypBest, arraysBest))]
for j in range(countBest):
    print(sortedString[countBest - j - 1])
sortedString1 = [x for (y, x) in sorted(zip(arrayp, arrays))]
for j in range(countOther):
    print(sortedString1[countOther - j - 1])
