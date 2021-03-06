from collections import deque


def __starting_point():
    t = int(input().strip())
    for _ in range(t):
        num_cnt = int(input().strip())
        deq = deque(list(map(int, input().strip().split(' '))))
        prev = max(deq[0], deq[-1])
        while deq:
            if prev >= deq[0] and prev >= deq[-1]:
                if deq[0] >= deq[-1]:
                    prev = deq.popleft()
                else:
                    prev = deq.pop()
            else:
                break
        if len(deq) == 0:
            print('Yes')
        else:
            print('No')


__starting_point()
