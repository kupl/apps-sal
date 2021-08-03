class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res=0
        rowDict=collections.defaultdict(int) 
        for r,c in reservedSeats:
          #row=r[0]
          #seatNo=r[1]
            rowDict[r] |=  (1 << (c-1))
        for row in rowDict.values():
            #p1=false, p2=false, p3=false
            print(\"row:\",row)
            p1=not(row & int('0111100000',2))
            p2=not(row & int('0000011110',2))
            p3=not(row & int('0001111000',2))
            print(p1,p2,p3)
            if p1 and p2:
                res+=2;
            elif p1 or p2 or p3:
                res+=1
            else:
                continue
        return res +2 *(n-len(rowDict))
