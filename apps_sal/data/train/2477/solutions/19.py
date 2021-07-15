class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        res, count, ct = 0, [], collections.Counter
        
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
        
        i = 0
        while i < len(count):
            j = i + 1
            while j < len(count):
                if count[i][0] == count[j][0] and count[i][1] == count[j][1]:
                    count.pop(j)
                    j -= 1
                j += 1
            res += 1
            count.pop(i)
        
        return res
