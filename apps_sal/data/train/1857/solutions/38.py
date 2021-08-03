class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seat_dict = {}
        all_possible_seats = [set([2, 3, 4, 5]), set([4, 5, 6, 7]), set([6, 7, 8, 9])]

        for row_seat in reservedSeats:
            row, seat = row_seat
            temp = seat_dict.get(row, [1, 1, 1])

            if sum(temp) == 0:
                continue

            if seat in all_possible_seats[0]:
                temp[0] = 0
            if seat in all_possible_seats[1]:
                temp[1] = 0
            if seat in all_possible_seats[2]:
                temp[2] = 0

            seat_dict[row] = temp
        # print(seat_dict)
        res = 0
        for row, situ in list(seat_dict.items()):
            if situ[1] == 1:
                if situ[0] and situ[2]:
                    res += 2
                else:
                    res += 1
            else:
                if situ[0] or situ[2]:
                    res += 1

        res += 2 * (n - len(list(seat_dict.keys())))
        return res
