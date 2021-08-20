class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        ans = 1
        target = [1] + target + [1]
        pre = 1
        _max = 1
        _min = 10 ** 9
        for i in range(len(target) - 1):
            if target[i] == 1:
                continue
            if target[i] <= target[i + 1]:
                _max = max(_max, target[i + 1])
            else:
                _min = min(_min, target[i + 1])
                _max = max(_max, target[i])
                ans += min(_max - pre, _max - 1)
                pre = _min
                _min = 10 ** 9
                _max = target[i + 1]
        return ans
