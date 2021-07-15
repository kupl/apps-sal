import heapq
def lemming_battle(n, g, b):
    g = [i*(-1) for i in g]
    b = [i*(-1) for i in b]
    heapq.heapify(g)
    heapq.heapify(b)
    while g and b:
        t1, t2 = [], []
        for _ in range(n):
            if len(g) == 0 or len(b) == 0:
                break
            x = heapq.heappop(g)*(-1)
            y = heapq.heappop(b)*(-1)
            if x > y:
                t1.append(x-y)
            elif x < y:
                t2.append(y-x)
        for i in t1:
            heapq.heappush(g, (-1)*i)
        for i in t2:
            heapq.heappush(b, (-1)*i)
    if len(g)==0 and len(b)==0:
        return "Green and Blue died"
    if len(g) == 0:
        x =' '.join(map(str, map(lambda x: x*(-1), sorted(b))))
        return 'Blue wins: {}'.format(x)
    else:
        x =' '.join(map(str, map(lambda x: x*(-1), sorted(g))))
        return 'Green wins: {}'.format(x)
