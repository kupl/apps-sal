from queue import PriorityQueue

taken = set()
adj = {}
pq = PriorityQueue()


def process(v, order):
    # order to be 1 or -1 to sort the priority_queue
    taken.add(v)
    for vi, w in adj[v]:
        if not vi in taken:
            pq.put((order * w, vi, v))


def make_spanning_tree(edges, t):
    edges_set = set()
    result = []
    adj.clear()
    taken.clear()
    first = ''
    order = 1 if t == 'min' else -1
    for edge in edges:
        u, v = edge[0]
        edges_set.add(edge)
        w = edge[1]
        if u == v:
            continue
        if not u in adj:
            adj[u] = []
        if not v in adj:
            adj[v] = []
        adj[u].append((v, w))
        adj[v].append((u, w))
        if not first:
            first = u

    process(first, order)
    mst_cost = 0
    while not pq.empty():
        w, u, v = pq.get()
        w = order * w
        if not u in taken:
            mst_cost += w
            process(u, order)
            result.append((v + u, w))
    for ri in range(len(result)):
        r = result[ri]
        if not r in edges_set:
            result[ri] = r[0][1] + r[0][0], r[1]
            

    return result  # vertices of a spanning tree


