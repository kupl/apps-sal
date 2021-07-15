class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        result = list(range(1,m+1))
        temp = 0
        i = 0
        real = []
        for i in range(len(queries)):
            for j in range(len(result)):
                if(queries[i] == result[j]):
                    real.append(j)
                    #print('position', j)
                    result.pop(j)
                    result.insert(0, queries[i])
                    #print(result)
                    continue
        return real
            

