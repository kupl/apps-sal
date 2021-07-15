class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = [0]*37
        for i in range(1,n+1):
            t,i = divmod(i,1000)
            h,i = divmod(i,100)
            ten,i = divmod(i,10)
            groups[t + h + ten + i] += 1
        max = 0
        count = 0
        for g in groups:
            if g > max:
                max = g
                count = 1
            elif g == max:
                count += 1                
        return count
            
        

