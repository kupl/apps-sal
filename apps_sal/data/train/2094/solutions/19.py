import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()


n = int(input())
s = input()
d = defaultdict(int)


one = s.count("n")
zero = s.count("z")

for i in range(one):
    print("1", end=" ")
for i in range(zero):
    print("0", end=" ")
