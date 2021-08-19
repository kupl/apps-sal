from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        # let A be length of A and B be length of B
        # let N be length of longest word in A
        # let M be length of longest word in B

        # time: O(AN + BM)
        # space: O(AN + M)
        counts_A = [Counter(a) for a in A]
        word_B = Counter()
        for b in B:
            for k, v in Counter(b).items():
                if k not in word_B or word_B[k] < v:
                    word_B[k] = v

        # time: O(AM)
        # space: O(A)
        ans = []
        for i, a in enumerate(counts_A):
            ind = 1
            for letter in word_B.keys():
                if letter not in a or a[letter] < word_B[letter]:
                    ind = 0
                    break
            if ind:
                ans.append(A[i])
        return ans
