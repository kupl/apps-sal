class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ans = []
        word = {}
        for i in B:
            for j in set(i):
                if j not in word:
                    word[j] = i.count(j)
                elif i.count(j) > word[j]:
                    word[j] = i.count(j)
        for i in A:
            x = 0
            for k in word:
                if word[k] > i.count(k):
                    x = 1
                    break
            if x != 1:
                ans.append(i)
        return ans
