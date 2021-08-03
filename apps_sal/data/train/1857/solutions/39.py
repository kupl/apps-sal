class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        hsh = {}

        for i in reservedSeats:
            row = i[0] - 1
            seat = i[1] - 1

            if row not in hsh:
                hsh[row] = [True for i in range(10)]

            hsh[row][seat] = False

        count = (n - len(hsh)) * 2
        for row in hsh:
            cnt = 0
            cou = 0
            for i in range(10):
                if hsh[row][i]:

                    if i in (3, 7) and cnt % 2 == 1:
                        cnt -= 1
                    cnt += 1
                    if cnt == 4:
                        cou += 1
                        cnt = 0
                else:
                    cnt = 0
            count += cou

        return count
