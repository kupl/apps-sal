from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        total = Counter()

        for word in B:
            counts = Counter(word)
            for ch, count in list(counts.items()):
                total[ch] = max(total[ch], count)

        result = []
        for word in A:
            counts = Counter(word)

            is_universal = True
            for ch, count in list(total.items()):
                if counts[ch] < count:
                    is_universal = False
                    break

            if is_universal:
                result.append(word)

        return result
