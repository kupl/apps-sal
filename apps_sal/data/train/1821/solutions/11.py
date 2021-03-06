class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left_list, right_list):
            if not left_list:
                return right_list
            if not right_list:
                return left_list
            left_ptr = right_ptr = 0
            out = []
            while left_ptr < len(left_list) and right_ptr < len(right_list):
                if left_list[left_ptr] <= right_list[right_ptr]:
                    out.append(left_list[left_ptr])
                    left_ptr += 1
                else:
                    out.append(right_list[right_ptr])
                    right_ptr += 1
            out.extend(left_list[left_ptr:])
            out.extend(right_list[right_ptr:])
            return out
        new_list = [[num] for num in nums]
        while len(new_list) > 1:
            out = []
            i = 0
            for i in range(0, len(new_list), 2):
                if i == len(new_list) - 1:
                    merged_list = merge(new_list[i], [])
                else:
                    merged_list = merge(new_list[i], new_list[i + 1])
                out.append(merged_list)
            new_list = out
        return new_list[0]
