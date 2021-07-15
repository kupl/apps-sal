from heapq import heapify, heappush, heappop 
def add_all(lst): 
    heapify(lst) 
    s=0
    print(lst)
    while len(lst)>1:
        m1=heappop(lst)
        m2=heappop(lst)
        s+=m1+m2
        if not lst: return s
        heappush(lst,m1+m2)

    #heap: 1,2,3,4,5    3
    #      3,3,4,5      6
    #      6,4,5        9
    #      9,6          15
    #      15

