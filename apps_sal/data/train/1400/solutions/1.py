# cook your dish here
for i in range(int(input())):
    n, l, r = list(map(int, input().split()))
    mins = 0
    maxs = 0
    start = 1
    end = 2 ** (min(r, n) - 1)
    cend = end
    reached = True
    add = True
    for j in range(n):
        mins += start
        if j + 1 == l:
            reached = False
            start = 1
        elif reached:
            start *= 2

    reached = True
    for j in range(n):
        maxs += end
        if j + 1 == r:
            reached = False
            end = cend
        elif reached:
            end = end // 2
    print(mins, maxs)
