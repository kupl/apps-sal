import sys
t = int(sys.stdin.readline().strip())
for i in range(t):
    votes = {}
    n = int(sys.stdin.readline().strip())
    for j in range(n):
        s, v = sys.stdin.readline().strip().split(' ')
        if v == '+':
            votes[s] = 1
        else:
            votes[s] = -1
    print(sum(votes.values()))
