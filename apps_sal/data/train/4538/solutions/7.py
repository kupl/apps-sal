def reverse_fun(n):
    from collections import deque as dq
    n = dq(n)
    n_dq = dq()
    for i in range(len(n)):
        if i == 0 or i % 2 == 0:
            n_dq.append(n.pop())
        elif i % 2 != 0:
            n_dq.append(n.popleft())
    return ''.join(n_dq)
