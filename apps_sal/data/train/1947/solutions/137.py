class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        universe = defaultdict(int)
        for b in B:
            bCount = defaultdict(int)
            for letter in b:
                bCount[letter] += 1
            for key in bCount:
                universe[key] = max(universe[key],bCount[key])
        
        # print(universe)
        
        result = []
        for a in A:
            aCount = defaultdict(int)
            for letter in a:
                aCount[letter] += 1
            isUni = True
            for letter in universe:
                if universe[letter] > aCount[letter]:
                    isUni = False
                    break
                else:
                    pass
            if isUni:
                result.append(a)
                
        return result
