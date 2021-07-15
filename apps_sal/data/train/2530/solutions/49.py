class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        dic = collections.defaultdict(lambda: 0)
        for i in range(len(time)) :
            
            time[i] = time[i] % 60
            dic[time[i]] += 1
        
        A = list(set(time))
        
        count_60 = dic[0]
        count_30 = dic[30]
        res = 0
        dic2 = {}
        print(A)
        for i in range(len(A)) :
            if A[i] % 30 != 0 :
                if A[i] not in dic2 :
                    dic2[60 - A[i]] = dic[A[i]]
                else:
                    res = res + dic2[A[i]] * dic[A[i]]
            print(res)
                    
        res = res + int(count_60 * 0.5 * (count_60 - 1)) + int(count_30 * 0.5 * (count_30 - 1))
        
        return res
                
                
        
        
        
        
                
                
            
            
            
        
        

