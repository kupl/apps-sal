class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        k = 1
        ans = [0, 1]
        while k <= n - 1:
            l = len(ans)
            for i in range(l - 1, -1, -1):
                ans.append((2**k) + ans[i])
            k = k + 1
        while 1:
            if ans[0] == start:
                break
            else:
                ans.append(ans.pop(0))
        return ans
