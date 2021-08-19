class Solution:

    def numSpecialEquivGroups(self, A: List[str]) -> int:
        (res, count, ct) = (0, [], collections.Counter)
        for s in A:
            even = collections.defaultdict(int)
            odd = collections.defaultdict(int)
            isEven = True
            for c in s:
                if isEven:
                    even[c] += 1
                else:
                    odd[c] += 1
                isEven = not isEven
            count.append((even, odd))
        while count:
            (i, count2) = (1, [])
            for i in range(1, len(count)):
                if count[0][0] != count[i][0] or count[0][1] != count[i][1]:
                    count2.append(count[i])
            res += 1
            count = count2
        return res
