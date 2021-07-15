class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        table = defaultdict(int)
        
        c = 0
        for i,t in enumerate(time):
            if (60-(t%60))%60 in table:
                c+=table[(60-(t%60))%60]
            table[(t%60)] +=1
        return c
        

