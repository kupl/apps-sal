class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rowHash = dict()
        numGroups = 0
        
        for res in reservedSeats:
            if res[0] in rowHash:
                rowHash[res[0]][res[1]] = True
            else:
                rowHash[res[0]] = dict()
                rowHash[res[0]][res[1]] = True
        
        for row in rowHash:
            # print(\"curr row \" + str(row) + \": \" + str(rowHash[row]))
            currGroups = 0

            if 2 not in rowHash[row] and \\
                3 not in rowHash[row] and \\
                4 not in rowHash[row] and \\
                5 not in rowHash[row]:
                currGroups += 1

            if 6 not in rowHash[row] and \\
                7 not in rowHash[row] and \\
                8 not in rowHash[row] and \\
                9 not in rowHash[row]:
                currGroups += 1

            if currGroups == 0 and \\
                4 not in rowHash[row] and \\
                5 not in rowHash[row] and \\
                6 not in rowHash[row] and \\
                7 not in rowHash[row]:
                currGroups += 1

            numGroups += currGroups

            # numGroups += int((nextSeat - currSeat - 1) / 4)
            # print(\"-> num groups:\" + str(numGroups))
        
        return numGroups + 2 * (n - len(rowHash))
        
\"\"\"
BCR: O(n)

Test cases:
n = 2, reservedSeats = [[2,1], [1,8], [2,6]]
- Only care about rows
- Sort it by row, then by seat # (O(klogk), where k is # of reservations)
[[1,8], [2,1], [2,6]]


n = 3
rowHash:    [1:[0,8,11], 2:[0, 1, 6, 11]]
row:        1
numGroups:  0 -> 1 -> 2 -> 3 -> 5

Approach:
- Brute force - reserve entire matrix 10 x n, populate reservations, iterate over each seat, finding chunks of 4 and marking them as reserved as we count. O(10n + k) where n is num rows and k is num reservations
- Sorted reservations
    - For each row without reservations, add int(10 / GROUP_SIZE=4)
    - For each row with reservations, iterate over each seat and calculate number of seats
    - Optimizations:
        - instead of sorting, use a hash map for rows
        - Need to track rows with and without any reservations (also use a heap?)
            - Otherwise cost for finding empty rows is O(n). this overhead is acceptable

\"\"\"
