class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # Reduce to Single Word in B
        # Time  complexity: O(A + B) where A and B is the total amount of information in A and B respectively.
        # Space complexity: O(A.length + B.length)
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)

        return ans
