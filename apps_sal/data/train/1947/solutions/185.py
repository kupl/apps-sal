import collections as clc


class Solution:

    def subset(self, counter1: clc.Counter, counter2: clc.Counter) -> bool:
        return all((cnt1 <= counter2[char] for (char, cnt1) in counter1.items()))

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        max_b_counter = clc.Counter()
        for b in B:
            for (char, cnt) in clc.Counter(b).items():
                max_b_counter[char] = max(max_b_counter[char], cnt)
        ans = []
        for a in A:
            if self.subset(max_b_counter, clc.Counter(a)):
                ans.append(a)
        return ans
