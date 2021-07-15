from heapq import *

def closure_gen(*s):
    keys,seen=set(s),set(s)
    q=sorted(seen)
    while q:
        curr=heappop(q)
        for next in [v for v in [curr*i for i in keys] if not v in seen]:
            heappush(q,next)
            seen.add(next)
        yield curr            

