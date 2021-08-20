from collections import deque


def loose_change(coins_list, amount_of_change):
    q = deque([(0, amount_of_change)])
    while q:
        (l, a) = q.popleft()
        if a == 0:
            return l
        q.extend(((l + 1, a - i) for i in coins_list if a >= i))
