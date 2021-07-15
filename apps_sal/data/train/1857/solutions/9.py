class Solution:
    # Process only rows that appear in the input, for other rows you can always allocate seats for two families.
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res, lookup = 0, collections.defaultdict(list)
        for i, j in reservedSeats:
            lookup[i].append(j - 1)
        for i in list(lookup.keys()):
            used = False
            # available size = 10, starting from 0.
            available = [1 for j in range(10)]
            # print('available = {0}, lookup[i] = {1}'.format(available, lookup[i]))
            for j in lookup[i]:
                available[j] = 0
            for start, end in [(1, 5), (5, 9)]:
                if sum(available[start: end]) == 4:
                # if all(j not in lookup[i] for j in range(start, end)):
                    res += 1
                    used = True
            if not used and sum(available[3:7]) == 4:
            # if not used and all(j not in lookup[i] for j in range(4, 8)):
                res += 1
        res += 2 * (n - len(lookup))
        return res
                    
                    

