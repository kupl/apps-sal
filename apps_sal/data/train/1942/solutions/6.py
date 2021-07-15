class Solution:
    def peopleIndexes(self, f: List[List[str]]) -> List[int]:
        
        ans = []
        l = 0
        flag = False
        for lists in f:
            flag = False
            for lists2 in f:
                # print(lists)
                # print(lists2)
                if(lists == lists2):
                    continue
                if set(lists).issubset(set(lists2)):
                    # print(\"in\
\")
                    flag = True
                    break
            if flag == False:
                ans.append(l)
                    
            l = l+1   
            
        return ans
        
