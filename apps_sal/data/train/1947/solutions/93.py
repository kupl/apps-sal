from functools import reduce


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        b_cnt = reduce(lambda a, b: Counter(a) | Counter(b), B)
        a_cnt = Counter()
        result = []

        for word in A:
            for w in word:
                if w in b_cnt:
                    a_cnt[w] += 1
            if not b_cnt - a_cnt:
                result.append(word)
            a_cnt.clear()

        return result
