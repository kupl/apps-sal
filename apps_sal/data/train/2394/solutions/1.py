import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
t = int(input())
for t1 in range(t):
    n = int(input())
    s = input()
    s = s.strip()
    l = []
    l.append(s[0])
    for i in range(1, n):
        if(s[i] == ")" and len(l) > 0 and l[-1] == "("):
            l.pop()
        else:
            l.append(s[i])
    print(len(l) // 2)
