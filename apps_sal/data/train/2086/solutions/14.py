from collections import deque
(n, m) = map(int, input().split())
t_deq = deque(list(map(int, input().split())))
t_quer = [int(input()) for x in range(m)]
a = max(t_deq)
t_wyn = []
count = 1
l_t_deq = len(t_deq) - 1
while True:
    t_wyn.append([t_deq[0], t_deq[1]])
    if t_deq[0] < t_deq[1]:
        t_deq.append(t_deq.popleft())
    else:
        c = t_deq.popleft()
        t_deq.append(t_deq.popleft())
        t_deq.appendleft(c)
    count += 1
    if t_deq[0] == a:
        break
for x in t_quer:
    if x < count:
        print(t_wyn[x - 1][0], t_wyn[x - 1][1])
    else:
        co = (x - count) % l_t_deq
        print(t_deq[0], t_deq[co + 1])
