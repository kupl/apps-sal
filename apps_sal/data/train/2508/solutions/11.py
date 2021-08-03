class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_arry = []
        for x in heights:
            sorted_arry.append(x)
        for i in range(len(sorted_arry)):
            curr_ele = sorted_arry[i]
            j = i + 1
            curr_index = i
            while(j < len(sorted_arry)):
                if curr_ele > sorted_arry[j]:
                    curr_ele = sorted_arry[j]
                    curr_index = j
                j = j + 1
            sorted_arry[curr_index] = sorted_arry[i]
            sorted_arry[i] = curr_ele
        change_count = 0
        for i in range(len(heights)):
            if heights[i] != sorted_arry[i]:
                change_count = change_count + 1
        return change_count
