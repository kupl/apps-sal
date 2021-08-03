import sys

t = int(input())

while t > 0:
    n = int(input())
    minimum = sys.maxsize
    while n > 0:
        s = input()
        minimum = min(minimum, s.count('a'), s.count('b'))
        n = n - 1
    print(minimum)
    t = t - 1
