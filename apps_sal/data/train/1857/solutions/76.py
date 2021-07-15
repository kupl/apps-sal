class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(set)
        for i, j in reservedSeats:
            if j in {2, 3, 4, 5}:
                seats[i].add(0)
            if j in {4, 5, 6, 7}:
                seats[i].add(1)
            if j in {6, 7, 8, 9}:
                seats[i].add(2)
        # For n rows, the maximum number of families that can sit together are 2*n.
        result = 2 * n
        for i in seats:
            if len(seats[i]) == 3:
                #  if all three positions in the row was blocked, the total cnt should be reduced by 2
                result -= 2
            else:
                # If less than 3 positions was blocked, the total cnt should -1.
                result -= 1
        return result

