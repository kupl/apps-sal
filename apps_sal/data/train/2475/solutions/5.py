class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        ans = 0
        for (i, word) in enumerate(zip(*A)):
            for j in range(len(word) - 1):
                if word[j] > word[j + 1]:
                    ans += 1
                    break
        return ans
