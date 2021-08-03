class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        out =[]
        temp=[]
        if len(groupSizes)>1:
            for each in range(len(groupSizes)):
                if type(groupSizes[each]) == int:
                    temp.append(each)
                    while len(temp) != groupSizes[each]:
                        for every in range(each+1,len(groupSizes)):
                            if groupSizes[each]==groupSizes[every]:
                                temp.append(every)
                                groupSizes[every]= \"x\"
                                break
                    out.append(temp)
                    temp=[]
        else:
            return [[0]]
        return out
                    
            
