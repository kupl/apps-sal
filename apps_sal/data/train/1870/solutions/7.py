class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        ans = [-1, -1, -1, -1, -1]
        
        for i in range(256):
            if count[i]>0:
                ans[0] = i
                break
        
        for i in range(255, -1, -1):
            if count[i]>0:
                ans[1] = i
                break
        
        s, n = 0, 0
        
        for i in range(256):
            s += i*count[i]
            n += count[i]
        
        ans[2] = s/n
        
        if n%2==0:
            acc = 0
            m1, m2 = -1, -1
            
            for i in range(256):
                acc += count[i]
                
                if acc>=n//2 and m1==-1:
                    m1 = i
                
                if acc>=n//2+1 and m2==-1:
                    m2 = i
                    break
                
            ans[3] = (m1+m2)/2
        else:
            acc = 0
            
            for i in range(256):
                acc += count[i]
                
                if acc>=n//2+1:
                    ans[3] = i
                    break
        
        M = 0
        
        for i in range(256):
            if count[i]>M:
                M = count[i]
                ans[4] = i
        
        return ans
