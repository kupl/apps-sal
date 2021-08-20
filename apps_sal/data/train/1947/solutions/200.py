class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        max_counts = collections.defaultdict(int)
        for b in B:
            counts = collections.Counter(b)
            for (char, count) in list(counts.items()):
                max_counts[char] = max(max_counts[char], count)
        universals = []
        for a in A:
            counts = collections.Counter(a)
            for (char, max_count) in list(max_counts.items()):
                if counts[char] < max_count:
                    break
            else:
                universals.append(a)
        return universals
