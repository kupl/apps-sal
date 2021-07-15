class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        
        max_set = {}
        result = []
        
        for i in B:
            for char in i:
                if char not in max_set:
                    max_set[char] = i.count(char)
                else:
                    max_set[char] = max(i.count(char), max_set[char])
        
        for word in A:
            flag = True
            for char in max_set:
                if word.count(char) < max_set[char]:
                    flag = False
                    break
            if flag:
                result.append(word)
            else:
                pass
            
        
        return result
                    

