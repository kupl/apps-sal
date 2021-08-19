class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        goal_count = len(arr) * 0.25
        temp_list = []
        for num in arr:
            if len(arr) == 1:
                return arr[0]
            elif len(temp_list) > goal_count:
                return temp_list[0]
            elif num in temp_list:
                temp_list.append(num)
            else:
                temp_list.clear()
                temp_list.append(num)
        return temp_list[0]
