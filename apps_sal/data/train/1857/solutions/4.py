class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seatOcc = set()
        rowsOcc = set()
        for i, j in reservedSeats:
            seatOcc.add((i - 1, j - 1))
            rowsOcc.add(i - 1)

        count = 2 * (n - len(rowsOcc))
        for i in rowsOcc:
            left = (i, 1) not in seatOcc and (i, 2) not in seatOcc and (i, 3) not in seatOcc and (i, 4) not in seatOcc
            mid = (i, 3) not in seatOcc and (i, 4) not in seatOcc and (i, 5) not in seatOcc and (i, 6) not in seatOcc
            right = (i, 5) not in seatOcc and (i, 6) not in seatOcc and (i, 7) not in seatOcc and (i, 8) not in seatOcc

            if(left and right):
                count += 2
            elif(left or mid or right):
                count += 1

        return count
