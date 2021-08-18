import sys

reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__

t = int(input())
for _ in range(t):
    s = int(input())
    spent = 0
    while s >= 10:
        cashback = s // 10
        spent += cashback * 10
        s = s % 10 + cashback
    spent += s
    print(spent)
