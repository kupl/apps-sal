from heapq import heappush,heappop
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        hashmap = {}
        for i in range(len(barcodes)):
            key = barcodes[i]
            if key not in hashmap:
                hashmap[key] = 1
            else:
                hashmap[key] = hashmap[key]+1
        h = []
        for key,val in list(hashmap.items()):
            heappush(h,(-val,key))
        result = [ ]
        tlist = []
        while h:
            pending_lst = []
            for i in range(2):
                if h:
                    frequency, char = heappop(h)
                    positive_frequency = -frequency
                    if positive_frequency > 0:
                        pending_lst.append((positive_frequency-1, char))
                        if result and char == result[-1]:
                            continue
                        result.append(char)
            if not h and not pending_lst:
                break
            for frequency, char in pending_lst:
                heappush(h, (-frequency, char))
        return result
                    
        
        
            

