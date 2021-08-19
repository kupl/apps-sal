class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        import heapq
        n = len(barcodes)
        d = {}
        for x in barcodes:
            if(d.get(x) != None):
                d[x] += 1
            else:
                d[x] = 1
        barcodes = []
        for x in list(d.keys()):
            heapq.heappush(barcodes, (-d[x], x))
        ans = []
        for x in range(n):
            temp = []
            if(ans == []):
                curr = heapq.heappop(barcodes)
                ans.append(curr[1])
                if(curr[0] != -1):
                    heapq.heappush(barcodes, (curr[0] + 1, curr[1]))
                # print(barcodes)
            else:
                while(True):
                    # print(barcodes,ans)
                    curr = heapq.heappop(barcodes)
                    if(ans[-1] != curr[1]):
                        ans.append(curr[1])
                        if(curr[0] != -1):
                            heapq.heappush(barcodes, (curr[0] + 1, curr[1]))
                        break
                    else:
                        temp.append(curr)
                while(len(temp)):
                    heapq.heappush(barcodes, temp.pop())
        return ans
