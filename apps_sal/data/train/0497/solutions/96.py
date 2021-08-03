class Solution:
    # Without cache, O(2^n log n) time, O(1) space; with cache, O(n x log n) time, O(n) space
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        A = sorted(zip(startTime, endTime, profit))
        n = len(A)

        def find_next_starting_point(cur_starting_point, start_time):
            if cur_starting_point >= n:
                return cur_starting_point

            left, right = cur_starting_point, n - 1
            while left + 1 < right:
                mid = left + (right - left) // 2
                if A[mid][0] < start_time:
                    left = mid
                else:
                    right = mid

            if A[left][0] >= start_time:
                return left
            # left < start_time
            if A[right][0] >= start_time:
                return right
            # right < start_time
            return right + 1

        cache = {n: 0}

        def find_max_profit(i):
            if i in cache:
                return cache[i]

            next_start = find_next_starting_point(i + 1, A[i][1])
            with_cur_task = A[i][2] + find_max_profit(next_start)
            without_cur_task = find_max_profit(i + 1)
            cache[i] = max(with_cur_task, without_cur_task)
            return cache[i]

        return find_max_profit(0)

    # O(n x log n) time, O(n) space
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        A = sorted(zip(endTime, startTime, profit))
        n = len(A)

        # The biggest profit as of the ith task
        cache = [0] * (n + 1)

        def find_closest_ending_point(cur_ending_point, end_time_limit):
            if cur_ending_point < 0:
                return 0

            left, right = 0, cur_ending_point
            while left + 1 < right:
                mid = left + (right - left) // 2
                if A[mid][0] <= end_time_limit:
                    left = mid
                else:
                    right = mid

            if end_time_limit >= A[right][0]:
                return right + 1
            # end_time_limit < right
            if end_time_limit >= A[left][0]:
                return left + 1
            # end_time_limit < left
            return left

        for i in range(1, n + 1):
            index = find_closest_ending_point(i - 2, A[i - 1][1])
            cache[i] = max(cache[i - 1], cache[index] + A[i - 1][2])

        return cache[n]
