class Solution:
    def sortString(self, s: str) -> str:
        sforward = sorted(s)
        sbackward = sforward[-1]
        
        suniq = ''
        
        for i in s:
            if i not in suniq:
                suniq += i

        suniq = sorted(suniq)
        
        max_count = 0
        
        for i in suniq:
            if s.count(i) > max_count:
                max_count = s.count(i)
        
        
        chr_count = [0 for i in range(len(suniq))]
           
        

        s_sort = ''
        
        for j in range(max_count):
            
            
            for i in range(len(suniq)):
                if chr_count[i] < s.count(suniq[i]):
                    s_sort += suniq[i]
                    chr_count[i] += 1
                else:
                    continue
                    
            suniq = suniq[::-1]
            chr_count = chr_count[::-1]
            
        
        return s_sort        
            

