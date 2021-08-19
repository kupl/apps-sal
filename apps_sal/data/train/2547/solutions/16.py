class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # counter set to 0
        counter = 0

        # loop thru arr of arr
        for arr in grid:

            # loop thru every single num in arr
            for num in arr:

                # if num is less than 0:
                if num < 0:
                    #counter += 1
                    counter += 1
        # return counter
        return counter
