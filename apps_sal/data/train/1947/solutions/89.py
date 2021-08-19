class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        def count(word):
            ans = [0] * 26
            for c in word:
                ans[ord(c) - ord('a')] += 1
            return ans
        B_dict = [0] * 26
        for b in B:
            for (i, c) in enumerate(count(b)):
                B_dict[i] = max(B_dict[i], c)
        ans = []
        for a in A:
            a_dict = count(a)
            flag = True
            for (i, c) in enumerate(count(a)):
                if c < B_dict[i]:
                    flag = False
                    break
            if flag:
                ans.append(a)
        return ans
