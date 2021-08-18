class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        queue = []
        ans = []
        for i in range(1, 10):
            queue.append(str(i))
        while len(queue) > 0:
            num = queue.pop(0)
            if len(num) == n and (num not in ans):
                ans.append(num)

            elif len(num) < n:
                x = int(num[-1])
                if x - k >= 0:
                    queue.append(num + str(x - k))
                if x + k <= 9:
                    queue.append(num + str(x + k))

        return ans
