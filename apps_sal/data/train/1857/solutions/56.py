class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = 0
        rows = defaultdict(list)
        for seat in reservedSeats:
            rows[seat[0]].append(seat[1])
        for row in list(rows.keys()):
            seat_nums = rows[row]
            if len(seat_nums) == 1:
                res = res + 2 if seat_nums[0] in [1, 10] else res + 1
            else:
                help_list = [0] * 10
                for seat in seat_nums:
                    help_list[seat - 1] = 1
                res_copy = res
                if help_list[1:5] == [0, 0, 0, 0]:
                    res += 1
                if help_list[5:9] == [0, 0, 0, 0]:
                    res += 1
                if res_copy == res and help_list[3:7] == [0, 0, 0, 0]:
                    res += 1
        return res + 2 * (n - len(list(rows.keys())))
