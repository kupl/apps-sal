from sys import stdin

# Input data
#stdin = open("input", "r")


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    d = {}
    for ele in arr:
        d[ele] = d.get(ele, 0) + 1
    cond = False
    for ele in d:
        if ele == 1000:
            if d[ele] >= 2:
                cond = True
                break
        else:
            if 2000 - ele in d:
                cond = True
                break
    if cond == True:
        print("Accepted")
    else:
        print("Rejected")
