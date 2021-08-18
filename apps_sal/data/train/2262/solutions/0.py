import sys
input = sys.stdin.readline


def main():
    R, C, N = map(int, input().split())
    xyxy = [list(map(int, input().split())) for i in range(N)]

    r = []

    for i in range(N):
        x1, y1, x2, y2 = xyxy[i]
        if ((x1 == 0 or x1 == R) or (y1 == 0 or y1 == C)) and ((x2 == 0 or x2 == R) or (y2 == 0 or y2 == C)):
            if x1 == 0:
                r.append((y1, i))
            elif x1 == R:
                r.append((C - y1 + C + R, i))
            elif y1 == 0:
                r.append((R - x1 + C * 2 + R, i))
            else:
                r.append((x1 + C, i))
            if x2 == 0:
                r.append((y2, i))
            elif x2 == R:
                r.append((C - y2 + C + R, i))
            elif y2 == 0:
                r.append((R - x2 + C * 2 + R, i))
            else:
                r.append((x2 + C, i))

    r = sorted(r)
    stack = []
    for i in range(len(r)):
        if len(stack) > 0:
            if stack[-1] == r[i][1]:
                stack.pop()
            else:
                stack.append(r[i][1])
        else:
            stack.append(r[i][1])

    if len(stack) > 0:
        print("NO")
    else:
        print("YES")


def __starting_point():
    main()


__starting_point()
