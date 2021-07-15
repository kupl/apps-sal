# Max heap
class Node:
    def __init__(self,x,y,d=None):
        self.x = x
        self.y = y
        if d:
            self.distance = d
        else:
            self.distance = x*x + y*y
        
        
def parent(i):
    return (i-1)//2
def left(i):
    return 2*i +1
def right(i):
    return 2*i +2
def swap(heap,i,j):
    t = heap[i]
    heap[i] = heap[j]
    heap[j] = t
    
def heapify(heap):
    n = len(heap)
    for i in range(1,n):
        p = parent(i)
        
        while i > 0 and heap[p].distance < heap[i].distance:
            # print(heap[i].distance,i,p)
            swap(heap,i,p)
            i = p
            p = parent(i)
        
    
def replace_top(heap,node):
    t = heap[0]
    heap[0] = node
    n = len(heap)
    # swap(heap,0,n-1)
    i = 0
    l = left(i)
    r = right(i)
    while i < n and not((l >= n or heap[l].distance <= heap[i].distance) and (r >= n or heap[r].distance <= heap[i].distance)):
        if l < n and r < n:
            if  heap[l].distance < heap[r].distance:
                swap(heap,i,r)
                i = r
            else:
                swap(heap,i,l)
                i = l
        elif l < n:
            swap(heap,i,l)
            i = l
        else:
            swap(heap,i,r)
            i = r
            
        l = left(i)
        r = right(i)
            
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        n = len(points)
        heap = []
        for i in range(K):
            p = points[i]
            node = Node(p[0],p[1])
            heap.append(node)
            # print(node.distance)
        heapify(heap)
        top = 0
        # print(heap)
        # print(\"max\",heap[top].distance)
        for i in range(K,n):
            p = points[i]
            
            distance = p[0]*p[0] + p[1]*p[1]
            # print(p,distance)
            if heap[top].distance > distance:
                node = Node(p[0], p[1], distance)
                # print(p,node.distance)
                replace_top(heap,node)
        return [ [heap[i].x,heap[i].y] for i in range(K)]
                
        

