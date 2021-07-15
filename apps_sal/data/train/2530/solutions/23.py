class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = 0
        
        ctr = collections.Counter(time)
        keys = []
                
        keys = list(ctr.keys())
        
        if len(keys) == 1:
            if keys[0] % 60 == 0:
                n = ctr[keys[0]] - 1
                cnt += n * (n + 1) / 2
                return int(cnt)
        
        for i in range(len(keys)):
            if keys[i] % 60 == 0 or keys[i] * 2 % 60 == 0:
                n = ctr[keys[i]] - 1
                cnt += int(n * (n + 1) / 2)
            
            
            
            for j in range(i+1, len(keys)):
                if (keys[i] + keys[j]) % 60 == 0:
                    cnt += ctr[keys[i]] * ctr[keys[j]]
        
        return cnt

    #store ctr + index and see the wrong ans input

