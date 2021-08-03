class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = sorted(reservedSeats, key=lambda x: x[0])
        a = set([2, 3])
        b = set([4, 5])
        c = set([6, 7])
        d = set([8, 9])
        i = 0
        ans = 0
        print(seats)
        seenRows = set()
        while i < len(seats):
            row = seats[i][0]
            r = row
            seenRows.add(row)
            j = i
            left, leftMiddle, rightMiddle, right = True, True, True, True
            while j < len(seats) and seats[j][0] == row:
                if seats[j][1] in a:
                    left = False
                elif seats[j][1] in b:
                    leftMiddle = False
                elif seats[j][1] in c:
                    rightMiddle = False
                elif seats[j][1] in d:
                    right = False
                j += 1
            ans += max(int(leftMiddle and rightMiddle), int(left and leftMiddle) + int(right and rightMiddle))
            i = j
        return ans + (n - len(seenRows)) * 2
