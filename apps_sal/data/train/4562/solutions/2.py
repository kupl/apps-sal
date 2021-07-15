from collections import deque

def snap(f,t):
    f, t = list(map(deque,(f,t)))
    m, snap = [], 0
    while t:
        for dq in (f,t):
            m.append(dq.popleft())
            if len(m)>1 and m[-2] == m[-1]:
                snap += 1
                f.extend(m)
                m.clear()
                break
    return snap 

