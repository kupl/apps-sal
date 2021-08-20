class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        ans = 1
        x = 0
        target = [1] + target + [1]
        n = len(target)
        pre = 1
        while x < n - 1:
            while x < n and target[x] == 1:
                x += 1
            if x == n:
                break
            while x < n - 1 and target[x] <= target[x + 1]:
                x += 1
            _max = target[x]
            while x < n - 1 and target[x] >= target[x + 1]:
                x += 1
            _min = target[x]
            pre = _min
            ans += min(_max - pre, _max - 1)
        return ans
