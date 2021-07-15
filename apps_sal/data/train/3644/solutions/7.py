from queue import PriorityQueue

def add_all(lst): 
    q = PriorityQueue()
    for x in lst: q.put(x)
    s = 0
    while q.qsize() > 1:
        a = q.get()
        b = q.get()
        s += a+b
        q.put(a+b)
    return s
