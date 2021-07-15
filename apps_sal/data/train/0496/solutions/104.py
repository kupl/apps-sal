from collections import defaultdict

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count_for_val = defaultdict(lambda:0)
        dups = set()
        for i in A:
            count_for_val[i] += 1
            if count_for_val[i] > 1:
                dups.add(i)
        output = 0
        dups = sorted(dups)
        if not len(dups):
            return 0
        orig = dups[0]
        for dup in dups:
            count = count_for_val[dup] - 1
            while count > 0:
                orig += 1
                if orig > dup and orig not in count_for_val:
                    count_for_val[orig] = 1
                    output = output + (orig - dup)
                    count -= 1
        return output
        
                

