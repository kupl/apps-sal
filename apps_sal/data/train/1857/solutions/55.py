class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = 0
        rows = defaultdict(list)
        #rows = {}
        for seat in reservedSeats:
            # if not rows.get(seat[0]):
            #rows[seat[0]] = [0]*10
            #rows[seat[0]][seat[1]-1] = 1
            rows[seat[0]].append(seat[1])
        print(rows)
        # for i in range(1, n+1):
        for row in list(rows.keys()):
            seat_nums = rows[row]
            #seat_nums = rows.get(i)
            # if not seat_nums:
            # print(f\"nothing in row {i}\")
            #    res+=2
            if len(seat_nums) == 1:
                # if seat_nums[0] == 1 or seat_nums[0] == 10:
                #    res+=2
                # else:
                #    res+=1
                # print(\"here\")
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
