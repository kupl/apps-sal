(n, q) = map(int, input().split())
stacks = [[] for i in range(n + 1)]
queue = []
q_start = 0
unread = 0
ans = []
for i in range(q):
    (action, num) = map(int, input().split())
    if action == 1:
        queue.append(0)
        stacks[num].append(len(queue) - 1)
        unread += 1
    elif action == 2:
        for i in range(len(stacks[num])):
            if stacks[num][i] >= q_start and queue[stacks[num][i]] == 0:
                queue[stacks[num][i]] = 1
                unread -= 1
        stacks[num] = []
    else:
        for i in range(q_start, num):
            if queue[i] == 0:
                queue[i] = 1
                unread -= 1
        q_start = max(q_start, num)
    ans.append(unread)
print('\n'.join(map(str, ans)))
