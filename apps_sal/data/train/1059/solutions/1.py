__author__ = 'Hacktivist'
from sys import stdin
lst = list()
testCase = int(stdin.readline().strip())
for test in range(testCase):
    lst.append(int(stdin.readline().strip()))
lst.sort()
if len(lst) <= 5000:
    maximum = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] % lst[j] > maximum:
                maximum = lst[i] % lst[j]
    print(maximum)
else:
    print(lst[len(lst) - 2] % lst[len(lst) - 1])
