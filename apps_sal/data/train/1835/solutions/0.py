class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # DFS (Depth-First Search)
        # Time  complexity: O(N x 2^N) = O(N x 9 x 2^(N-1))
        # Space compleixty: O(2^N) = O(9 x 2^(N-1)) + O(N)
        # if n == 1:
        #     return [i for i in range(10)]

        # ans = []
        # def dfs(n, num):
        #     # base case
        #     if n == 0:
        #         return ans.append(num)

        #     tail_digit = num % 10
        #     # using set() to avoid duplicates when K == 0
        #     next_digits = set([tail_digit + k, tail_digit - k])

        #     for next_digit in next_digits:
        #         if 0 <= next_digit < 10:
        #             new_num = num * 10 + next_digit
        #             dfs(n - 1, new_num)

        # for num in range(1, 10):
        #     dfs(n - 1, num)

        # return list(ans)

        # BFS (Breadth-First Search)
        # Time  complexity: O(N x 2^N)
        # Space complexity: O(2^N)
        if n == 1:
            return [i for i in range(10)]

        # initialize the queue with candidates for the first level
        queue = [digit for digit in range(1, 10)]

        for level in range(n - 1):
            next_queue = []
            for num in queue:
                tail_digit = num % 10
                # using set() to avoid duplicates when K == 0
                next_digits = set([tail_digit + k, tail_digit - k])

                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        new_num = num * 10 + next_digit
                        next_queue.append(new_num)

            # start the next level
            queue = next_queue

        return queue
