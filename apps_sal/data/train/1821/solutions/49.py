class Solution:
    def merge_sort(self, nums):
        def helper_sort(left, right):
            if left > right:
                return []
            if left == right:
                return [nums[left]]

            mid = (left + right) // 2
            l = helper_sort(left, mid)
            r = helper_sort(mid + 1, right)
            return helper_merge(l, r)

        def helper_merge(left_arr, right_arr):
            l_idx = 0
            r_idx = 0
            ret = []

            while l_idx < len(left_arr) and r_idx < len(right_arr):
                if left_arr[l_idx] < right_arr[r_idx]:
                    ret.append(left_arr[l_idx])
                    l_idx += 1
                else:
                    ret.append(right_arr[r_idx])
                    r_idx += 1
            ret.extend(left_arr[l_idx:])
            ret.extend(right_arr[r_idx:])
            return ret
        return helper_sort(0, len(nums) - 1)

    def merge_sort_iter(self, nums):
        if len(nums) <= 1:
            return nums
        q = deque()
        for n in nums:
            q.append([n])

        while len(q) > 1:
            size = len(q)
            idx = 0
            while idx < size:
                l_arr = q.popleft()
                idx += 1
                if idx == size:
                    q.append(l_arr)
                    break
                r_arr = q.popleft()
                idx += 1

                l_idx = 0
                r_idx = 0
                tmp = []
                while l_idx < len(l_arr) and r_idx < len(r_arr):
                    if l_arr[l_idx] < r_arr[r_idx]:
                        tmp.append(l_arr[l_idx])
                        l_idx += 1
                    else:
                        tmp.append(r_arr[r_idx])
                        r_idx += 1
                tmp.extend(l_arr[l_idx:])
                tmp.extend(r_arr[r_idx:])
                q.append(tmp)
        return q.popleft()

    def sortArray(self, nums: List[int]) -> List[int]:
        # return self.merge_sort(nums)
        return self.merge_sort_iter(nums)
