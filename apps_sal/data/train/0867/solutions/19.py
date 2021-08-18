import collections


def hit(bricks):
    if len(bricks) == 3:
        if sum(bricks) <= S:
            bricks.clear()
        else:
            if bricks[0] + bricks[1] <= S:
                bricks.popleft()
                bricks.popleft()
            else:
                if bricks[1] + bricks[2] <= S:
                    bricks.pop()
                    bricks.pop()
                else:
                    if bricks[2] <= S:
                        bricks.pop()
    elif len(bricks) == 2:
        if bricks[0] + bricks[1] <= S:
            bricks.popleft()
            bricks.popleft()
        else:
            if bricks[1] <= S:
                bricks.pop()
    elif len(bricks) == 1:
        if bricks[0] <= S:
            bricks.pop()
        else:
            raise ValueError("Last brick too stronk")

    return bricks


T = int(input())

for _ in range(T):
    S, W1, W2, W3 = list(map(int, input().split()))
    bricks = collections.deque([W1, W2, W3])
    count = 0

    while len(bricks) > 0:
        bricks = hit(bricks)
        count += 1

    print(count)
