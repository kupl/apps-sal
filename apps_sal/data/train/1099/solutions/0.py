import sys


def f(p):
    votes = {}
    for x in range(p):
        str = sys.stdin.readline()
        t = str.split()
        votes[t[0]] = t[1]

    ans = 0
    for per in votes:
        if votes[per] == "+":
            ans = ans + 1
        else:
            ans = ans - 1

    return ans


x = sys.stdin.readline()
for t in range(int(x)):
    p = sys.stdin.readline()
    print(f(int(p)))
