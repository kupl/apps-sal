'''input
4 6
1 2
1 4
1 2
3 3
1 3
1 3


'''

n, q = list(map(int, input().split()))

count = [0 for i in range(n + 1)]
queue = []
read = set()
unread = 0
ans = []
last_q_idx = 0
last_app_idx = [1 for i in range(n + 1)]

for i in range(q):
    action, num = list(map(int, input().split()))
    if action == 1:
        queue.append((num, count[num] + 1))
        count[num] += 1
        unread += 1
    elif action == 2:
        for number in range(last_app_idx[num], count[num] + 1):
            if (num, number) not in read:
                read.add((num, number))
                unread -= 1
        last_app_idx[num] = max(last_app_idx[num], count[num])
    else:
        for idx in range(last_q_idx, num):
            app, number = queue[idx]
            if (app, number) not in read:
                read.add((app, number))
                last_app_idx[app] = max(last_app_idx[app], number)
                unread -= 1
        last_q_idx = max(last_q_idx, num)
    ans.append(unread)

print("\n".join(map(str, ans)))
