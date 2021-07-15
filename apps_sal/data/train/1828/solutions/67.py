import collections
from heapq import heappush, heappop
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        elementCountMap = collections.Counter(barcodes)
        elementStack = []
        for element, count in list(elementCountMap.items()):
            heappush(elementStack, [-count, element])
        
        result = []
        
        previousElement = None
        
        while elementStack:
            tmp = None
            count, element = heappop(elementStack)
            if element == previousElement:
                tmp = [count, element]
                count, element = heappop(elementStack)
                
            result.append(element)
            previousElement = element
            count += 1
            if count < 0:
                heappush(elementStack, [count, element])
            
            if tmp:
                heappush(elementStack, tmp)
                
        return result

