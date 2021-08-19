class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        ans = Counter(A)
        return sorted(list(ans.keys()), key=lambda x: ans.get(x), reverse=True)[0]
