class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        dicta = collections.defaultdict(int)
        max_word = 0
        for i in barcodes:
            dicta[i]+=1
            if dicta[i]>dicta[max_word]:
                max_word = i
        
        n=len(barcodes)
        ans = [0 for i in range(n)]
        idx=0
        
        for i in range(dicta[max_word]):
            ans[idx] = max_word
            idx+=2    
        del dicta[max_word]
        #print(ans)
        #idx=1
        for let in dicta:
            for i in range(dicta[let]):
                if idx>=n:
                    idx=1
                ans[idx]=let
                idx+=2
        
        return ans

