class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        result = 0
    
        m = {}

        for s in (time):
            dif = 60 - s%60
            if(dif == 60):
                dif = 0
            if(dif in m):
                result+= m.get(dif)
            if(s%60 not in m):
                m.update({s%60:0})
            m.update({s%60:m.get(s%60)+1})
            # print(m)


        return result
    

