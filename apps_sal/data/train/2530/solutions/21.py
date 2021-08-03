class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod_counts = Counter(t % 60 for t in time)

        pairs_count = 0
        for mod, count in mod_counts.items():
            if mod == 0 or mod == 30:
                pairs_count += count * (count - 1) // 2
            elif mod < 30 and 60 - mod in mod_counts:
                pairs_count += count * mod_counts[60 - mod]

        return pairs_count
