import sys

s = sys.stdin.read()

n = 1000000007

aCount = 0
bCount = 0

count = 0

increment = 0

for c in s:
    if c == 'a':
        increment = (2 * increment + 1) % n

    if c == 'b':
        count = (count + increment) % n

print(count)
