class Solution:
    '''
    def minNumberOperations(self, target: List[int]) -> int:

        def get(num, dp):
            if not num:
                return 0
            numt = tuple(num)
            if numt not in dp:
                val = min(num)
                left = 0
                result = val
                for k in range(len(num)):
                    num[k] -= val
                    if num[k] == 0:
                        if left < k:
                            result += get(num[left:k], dp)
                        left = k + 1
                if left < len(num):
                    result += get(num[left:], dp)
                dp[numt] = result
            return dp[numt]

        dp = {}
        return get(target, dp)
    '''

    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        stack = [0]
        for k in target:
            while len(stack) >= 1 and stack[-1] >= k:
                ans += (stack[-1] - max(k, stack[-2]))
                stack.pop()
            stack.append(k)
        return ans + stack[-1]

    '''
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        current = 0
        for k in target:
            if k > current:
                ans += (k-current)
            current = k
        return ans
    '''
