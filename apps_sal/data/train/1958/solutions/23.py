class Solution:
    def groupThePeople(self, gr: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(gr)):
            count = gr[i]
            if(count != 0):
                temp = []
                for j in range(len(gr)):
                    for k in range(count):
                        if(gr[j] == count):
                            temp.append(j)
                            gr[j] = 0
                        if(len(temp) == count):
                            res.append(temp)
                            temp = []
                if(len(temp) != 0):
                    res.append(temp)
        return res
