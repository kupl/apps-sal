T = int(input())
for i in range(T):
    N = int(input())
    poly = [(0, 0) for j in range(N)]
    diff = [(0, 0) for j in range(N)]
    for j in range(N):
        poly[j] = list(map(int, input().split()))
        diff[j] = [poly[j][1] - 1, poly[j][0] * poly[j][1]]
    diff.sort()
    diff.reverse()
    for j in range(N):
        if j == 0:
            if diff[j][0] == -1:
                print(0, end=' ')
            elif diff[j][0] == 0:
                print("%d" % diff[j][1], end=' ')
            else:
                print("%dx^%d" % (diff[j][1], diff[j][0]), end=' ')
        else:
            if diff[j][0] == -1:
                break
            elif diff[j][0] == 0:
                print("+ %d" % diff[j][1], end=' ')
            else:
                print("+ %dx^%d" % (diff[j][1], diff[j][0]), end=' ')
    print("")
