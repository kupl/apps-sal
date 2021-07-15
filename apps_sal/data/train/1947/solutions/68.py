from collections import Counter
class Solution:
     def wordSubsets(self, A, B):
        count = collections.Counter()
        for b in B:
            count = count | collections.Counter(b)
        return [a for a in A if Counter(a) & count == count]
