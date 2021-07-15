class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        l=barcodes[::]
        n=len(l)
        c=Counter(l)
        c=list(sorted(list(c.items()),key=lambda x:-x[1]))
        nl=[0]*n
        y=0
        x=c[y][1]
        val=c[y][0]
        for i in range(0,n,2):
            nl[i]=val
            x-=1
            if x==0:
                y+=1
                if y<len(c):
                    x=c[y][1]
                    val=c[y][0]        
        for i in range(1,n,2):
            nl[i]=val
            x-=1
            if x==0:
                y+=1
                if y<len(c):
                    x=c[y][1]
                    val=c[y][0]
        return nl
            

