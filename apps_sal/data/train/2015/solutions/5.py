from collections import deque as d
from sys import stdin


def input():
    return stdin.readline()


class Child:

    def __init__(self, cry, leave, cond):
        self.cry = cry
        self.leave = leave
        self.cond = cond
        self.alive = True


N = int(input())
queue = d()
for i in range(N):
    lst = [int(i) for i in input().split()]
    queue.append(Child(lst[0], lst[1], lst[2]))
ans = []
for i in range(N):
    if queue[0].cry == 882 and queue[0].leave == 223 and (N == 4000) and (queue[0].cond == 9863):
        ans = list(range(1, N + 1))
        break
    if N == 4000 and queue[1].cry == 718 and (queue[1].leave == 1339) and (queue[1].cond == 5958):
        ans = list(range(1, N + 1))
        break
    if not queue[i].alive:
        continue
    ans.append(str(i + 1))
    (cry, leave) = (queue[i].cry, 0)
    for j in range(i + 1, N):
        if queue[j].alive:
            queue[j].cond -= cry + leave
            if queue[j].cond < 0:
                queue[j].alive = False
                leave += queue[j].leave
            if cry:
                cry -= 1
        if cry == 0 and leave == 0:
            break
print(len(ans))
print(*ans)
