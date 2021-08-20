class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        dup = []
        seen = set()
        for i in A:
            if i not in seen:
                seen.add(i)
            else:
                dup.append(i)
        curr = 0
        j = 0
        i = -1
        ans = 0
        print(seen)
        while j < len(dup):
            if i == dup[j]:
                curr = max(curr, i)
                while curr in seen:
                    curr += 1
                seen.add(curr)
                ans += curr - dup[j]
                j += 1
            else:
                i += 1
        return ans
