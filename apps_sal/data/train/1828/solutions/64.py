class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        d = collections.Counter(barcodes)
        res = []
        pq = []
        for no, f in list(d.items()):
            heapq.heappush(pq, [-f, no])
        temp = []
        while len(pq) != 0 or temp != 0:
            if(len(pq) != 0):
                f, no = heapq.heappop(pq)
                if(temp != []):
                    heapq.heappush(pq, temp)
                    temp = []
            else:
                if(temp != []):
                    f, no = temp
                    temp = []
                else:
                    break
            f = f * -1
            f = f - 1
            res.append(no)
            if(f != 0):
                if(len(pq) == 0):
                    heapq.heappush(pq, [-f, no])
                elif -f > pq[0][0]:
                    heapq.heappush(pq, [-f, no])
                else:
                    temp = [-f, no]

        return res
