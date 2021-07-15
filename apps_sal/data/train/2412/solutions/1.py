class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        list1 = []
        for i in S:
            if len(list1) > 0:
                if list1[-1] != i:
                    list1.append(i)
                else:
                    list1 = list1[:-1]
            else:
                list1.append(i)
            
        result = ''
        for i in list1:
            result += i
            
        return result
