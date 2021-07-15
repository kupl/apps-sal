class Solution:
    def containsPattern(self, arr: List[int], k: int, m: int) -> bool:
        i = 0
        
        n = len(arr)
        while(i + k < n):
            s = 0
            c = i
            lx = arr[c:c + k]
            while(c + k<= n):
                if(lx == arr[c:c + k]):
                    s += 1
                else:
                    break
                c += k
            if(s >= m):
                return True
            i += 1
        return False
            
                
        

