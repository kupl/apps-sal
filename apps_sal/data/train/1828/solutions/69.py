class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count=Counter(barcodes)
        heap=[(-count[x],x) for x in list(count.keys())]
        heapq.heapify(heap)
        out=[]
        while len(heap)>1:
            count1, code1=heapq.heappop(heap)
            count2, code2=heapq.heappop(heap)
            out.extend([code1,code2])
            count1+=1
            count2+=1
            if count1<0: heapq.heappush(heap, (count1,code1))
            if count2<0: heapq.heappush(heap, (count2,code2))
        if heap:
            count1,code1=heapq.heappop(heap)
            out+=[code1]
        return out

