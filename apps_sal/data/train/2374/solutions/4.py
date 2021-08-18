import sys
input = sys.stdin.readline

q = int(input())
for testcases in range(q):
    n = int(input())
    MAP = [list(map(int, list(input().strip()))) for i in range(2)]

    X = 0
    Y = 0
    fr = 0

    while True:
        if X == n and Y == 1:
            print("YES")
            break
        if X == n:
            print("NO")
            break

        if MAP[Y][X] <= 2:
            if fr == 0:
                fr = 0
                X += 1

            else:
                print("NO")
                break

        else:
            if fr == 0:
                fr = 1
                Y += 1
                Y %= 2
            else:
                X += 1
                fr = 0
