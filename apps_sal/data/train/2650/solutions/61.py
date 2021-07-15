import collections
import sys

m = collections.defaultdict(int)
line = input()
tokens = line.split()
n = int(tokens[0])
strings = []
for i in range(n):
    s = input()
    strings.append(s)

print(''.join(sorted(strings)))
