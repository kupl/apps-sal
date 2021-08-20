import heapq
import sys
input = sys.stdin.readline
(N, Q) = map(int, input().split())
event_list = []
for i in range(N):
    (S, T, X) = map(int, input().split())
    event_list.append((S - X - 0.5, 1, X))
    event_list.append((T - X - 0.5, -1, X))
dlist = []
for i in range(Q):
    D = int(input())
    event_list.append((D, 0, X))
    dlist.append(D)
event_list.sort()
answer_dic = {}
stop_set = set()
min_set = float('inf')
for (t, f, x) in event_list:
    if f == 1:
        stop_set.add(x)
        if x < min_set:
            min_set = x
    elif f == -1:
        stop_set.remove(x)
        if x == min_set:
            if len(stop_set) > 0:
                min_set = min(stop_set)
            else:
                min_set = float('inf')
    elif len(stop_set) > 0:
        answer_dic[t] = min_set
    else:
        answer_dic[t] = -1
for d in dlist:
    print(answer_dic[d])
