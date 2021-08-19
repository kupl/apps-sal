from sys import stdin
from collections import Counter
read = stdin.readline
for testcase in range(int(read())):
    length = int(read())
    string = read().strip()
    counts = Counter(string)
    odd_counts = 0
    for count in list(counts.values()):
        odd_counts += count % 2
    print(max(odd_counts - 1, 0))
