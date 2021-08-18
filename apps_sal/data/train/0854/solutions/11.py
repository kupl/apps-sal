from sys import stdin


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    d = {}
    for ele in arr:
        d[ele] = d.get(ele, 0) + 1
    for ele in d:
        if d[ele] > 1:
            print("ne krasivo")
            break
    else:
        print("prekrasnyy")
