class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        """
        Discuss Solution thats faster at detecting
        the number of requests that overlap an index.

        Key Idea have array t, loop
        through requests [[start, end] ...]

        Make t[start] += 1 to indicate
        every index after start is counted once
        for this request overlap
        Make t[end + 1] -= 1 to indicate
        every index after end + 1 is counted one less
        for this request overlap

        The prefix sum of array t tells us
        the number of requests that overlap
        an index

        requests
        [[0,2],[1,3],[1,1]]

          -
          - - -
        - - -
        0 1 2 3 4 5
        1 2 3 4 5 9

        t
        0  1  2  3  4  5  6
        1  2 -1 -1 -1

        t_prefix
        0  1  2  3  4  5  6
        1  3  2  1  0  0  0

        t.pop to remove index 6
        Sort both nums and t and
        use zip to line them up
        This matches most frequently
        overlapped index with biggest
        num.

        nums
        1 2 3 4 5 9
        t
        0 0 1 1 2 3

        Multiply because index i gets overlapped
        t[i] times so the nums value of mapping
        also gets mulitplied that number of times
        for the sum

        nums[i] * t[i]
        0 0 3 4 10 27

        sum of final = 44
        """
        t = [0] * (len(nums) + 1)
        for (start, end) in requests:
            t[start] += 1
            t[end + 1] -= 1
        for i in range(1, len(nums)):
            t[i] += t[i - 1]
        nums.sort()
        t.pop()
        t.sort()
        return sum((a * b for (a, b) in zip(nums, t))) % (10 ** 9 + 7)
