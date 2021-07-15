class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = {}
        
        # create frq
        for b in barcodes:
            if b in freq:
                freq[b] += 1
            else:
                freq[b] = 1
        
        frqBarcode = [(k, v) for (k, v) in list(freq.items())]
        maxNum, maxIncrements = max(frqBarcode, key=lambda i: i[1])
        
        newBarcode = [maxNum] * maxIncrements
        
        curIndex, curIncrements = 1, 0
        for num, count in frqBarcode:
            if num == maxNum:
                continue
            while count > 0:
                newBarcode.insert( curIndex, num )
                curIndex += 2
                maxIncrements += 1
                if curIncrements > maxIncrements or curIndex > len(newBarcode):
                    curIndex = 1
                    maxIncrements = 0
                count -= 1

        return newBarcode
                
        
        
                

