class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        #         # Ot(n^2) where n = len(dominoes)
        #         # Os(1)
        #         count, n = 0, len(dominoes)
        #         for i in range(n - 1):
        #             for k in range(i + 1, n):
        #                 count += dominoes[i] == dominoes[k] or dominoes[i] == list(reversed(dominoes[k]))

        #         return count

        #         # Ot(n) where n = len(dominoes)
        #         # Os(n)

        #         count_dict = {}
        #         total_count = 0
        #         for d1, d2 in dominoes:
        #             if (d1, d2) in count_dict:
        #                 count_dict[(d1, d2)] += 1
        #                 total_count += count_dict[(d1, d2)] - 1
        #             elif (d2, d1) in count_dict:
        #                 count_dict[(d2, d1)] += 1
        #                 total_count += count_dict[(d2, d1)] - 1
        #             else:
        #                 count_dict[(d1, d2)] = 1

        #         return total_count

        # Ot(n) where n = len(dominoes)
        # Os(n)

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
