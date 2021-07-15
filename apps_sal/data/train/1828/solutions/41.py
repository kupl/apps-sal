class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        h=collections.Counter(barcodes)
        heap=[(-value,key) for key,value in list(h.items())]
        heapq.heapify(heap)
        a=[]
        while heap:
            x=heapq.heappop(heap)
            if heap==[]:
                a.append(x[1])
                return a
            y=heapq.heappop(heap)
            a.append(x[1])
            a.append(y[1])
            if x[0]+1!=0:
                heapq.heappush(heap,(x[0]+1,x[1]))
            if y[0]+1!=0:
                heapq.heappush(heap,(y[0]+1,y[1]))
        return a
            

