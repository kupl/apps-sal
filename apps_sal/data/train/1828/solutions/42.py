class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = {}
        
        # create frq
        for b in barcodes:
            if b in freq:
                freq[b] += 1
            else:
                freq[b] = 1
        
        descBarcode = sorted([(k, v) for (k, v) in list(freq.items())], key=lambda i: i[1], reverse=True)
        # print(descBarcode)
        
        newBarcode = []
        maxIncrements = descBarcode[0][1] # -1
        
        curIndex, curIncrements = 1, 0
        for num, count in descBarcode:
            if not newBarcode:
                newBarcode = [num] * count
            else:
                while count > 0:
                    # print(f\"Inserting {num} at {curIndex}\", newBarcode)
                    newBarcode.insert( curIndex, num )
                    curIndex += 2
                    maxIncrements += 1
                    if curIncrements > maxIncrements or curIndex > len(newBarcode):
                        curIndex = 1
                        maxIncrements = 0
                    count -= 1
        
        # for i in range(len(newBarcode)):
        #     if i > 0 and newBarcode[i] == newBarcode[i-1]:
        #         newBarcode.pop(i)
        #         newBarcode.insert(0, newBarcode[i-1])
        # # print(newBarcode)
        return newBarcode
                
        
        
                

