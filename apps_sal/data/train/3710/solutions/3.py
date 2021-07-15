import heapq

def ulam_sequence(u0, u1, n):
    seq,h,s = [u0,u1],[u0+u1],set()
    while len(seq) < n:
        v=heapq.heappop(h); h=set(h)
        for u in seq:
            if u+v not in s: s.add(u+v); h.add(u+v)
            elif u+v in h: h.remove(u+v)
        seq.append(v); h=list(h); heapq.heapify(h)
    return seq
