class Solution:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count_dict = {}
        total_count = 0
        for d in dominoes:
            d = tuple(sorted(d))
            if d in count_dict:
                total_count += count_dict[tuple(d)]
                count_dict[d] += 1
            else:
                count_dict[d] = 1
        return total_count
