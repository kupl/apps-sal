class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n=len(barcodes)
        if n==1:
            return barcodes
        ans=[]
        barcodes.sort()
        if n%2==0:
            for x,y in zip(barcodes[:n//2],barcodes[n//2:]):
                ans.extend([y,x])
        else:
            mid=barcodes[n//2]
            added,x_last=0,-1 # added: flag indicating if the middle element is added to the result
            for x,y in zip(barcodes[:n//2],barcodes[n//2+1:]):
                if not added and x_last!=mid and y!=mid: 
                    ans.append(mid)
                    added=1
                ans.extend([y,x])
                x_last=x
            if not added:
                ans.append(mid)
        return ans

