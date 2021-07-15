class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        B_dict = collections.defaultdict(int)
        
        for elem in B: 
            elem_dict = collections.Counter(elem)
            for item in elem_dict: 
                B_dict[item] = max(B_dict[item], elem_dict[item])
        
        output = []
        for elem in A:
            found = True
            elem_dict = collections.Counter(elem)
            for item in B_dict:
                if item not in elem_dict or elem_dict[item] < B_dict[item]:
                    found = False
                    break
            if found:
                output.append(elem)
        
        return output
