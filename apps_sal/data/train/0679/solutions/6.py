import sys

N = eval(input())

ignore = [0]
name = []
arr = []
cname = cignore = 0
x = sys.stdin.readline().split()
arr.append(int(x[0]))
name.append(x[1])
for xyz in range(N - 1):
    x = sys.stdin.readline().split()
    if x[0] != "-1" and x[0] != "0":
        if cname == -1 or int(x[0]) <= arr[cname]:
            ignore.append(0)
            cignore = cignore + 1
            cname = cname + 1
            name.append(x[1])
            arr.append(int(x[0]))
        else:
            ignore[cignore] = ignore[cignore] + 1
    elif x[0] == "-1":
        aman = arr.pop()
        cignore = cignore - 1
        cname = cname - 1
        print(ignore.pop(), name.pop())
