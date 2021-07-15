class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        final_count = 0
        for arr_1_val in arr1:
            #store the matches
            correct_count = 0
            for arr_2_val in arr2:

                if abs(arr_1_val- arr_2_val) > d:
                    correct_count += 1
            if correct_count == len(arr2):
                final_count += 1
        return final_count

