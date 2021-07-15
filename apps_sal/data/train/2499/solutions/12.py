from collections import Counter
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if(len(deck) < 2): return False 
        deck_count = Counter(deck)
        v = set(deck_count.values())
        min_v = min(v)
        v_dict = dict()
        all_factors = set()
        for num in v :
            for j in range(2, min_v + 1):
                if(num % j == 0):
                    if(num in v_dict): v_dict[num].add(j)
                    else:
                        v_dict[num] = set()
                        v_dict[num].add(j)
                    all_factors.add(j)
        if(len(v_dict) != len(v)): return False
        for i in list(v_dict.values()):
            all_factors = all_factors.intersection(i)
        if(len(all_factors) > 0):
            return True
        return False
        

