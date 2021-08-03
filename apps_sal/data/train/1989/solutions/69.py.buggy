class Solution:\r
    def longestAwesome(self, s):\r
        def check(num):\r
            if num == 0:\r
                self.ans = i + 1\r
                return True\r
            elif seen[num] != float('inf'):\r
                self.ans = max(self.ans, i - seen[num])\r
                return True\r
            else:\r
                return False\r
\r
        # 0 ~ 2^10\r
        if not s:\r
            return 0\r
        seen = [float('inf') for _ in range(1024)]\r
        cur = 0\r
        self.ans = 0\r
        flips = [2 ** i for i in range(10)]\r
        for i, val in enumerate(s):\r
            mask = 2 ** int(val)\r
            cur ^= mask\r
            check(cur)\r
            for flip in flips:\r
                check(cur ^ flip)\r
            seen[cur] = min(i, seen[cur])\r
        \r
        return self.ans\r
                \r
print(Solution().longestAwesome('350844'))
