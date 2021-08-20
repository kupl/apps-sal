import sys
T = int(sys.stdin.readline().strip())
for t in range(0, T):
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    if max(a) > sum(a) / 2:
        print('T')
    elif sum(a) % 2 == 1:
        print('T')
    else:
        print('HL')
