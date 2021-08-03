class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        # fams = n*2
        res = {}
        for seat in reservedSeats:
            row, seat_n = seat
            if row in res:
                res[row].append(seat_n)
            else:
                res[row] = [seat_n]
        fams = 0
        for row in list(res.keys()):
            if len(res[row]) == 1:  # only one seat taken
                seat_n = res[row][0]
                if seat_n in [1, 10]:
                    fams += 2
                else:
                    fams += 1
            else:  # multiple seats taken
                curr_row = [True for i in range(10)]
                for s in res[row]:
                    curr_row[s - 1] = False
                edges = False
                if sum(curr_row[1:5]) == 4:
                    edges = True
                    fams += 1
                if sum(curr_row[5:9]) == 4:
                    edges = True
                    fams += 1
                if not edges and sum(curr_row[3:7]) == 4:
                    fams += 1
        fams += ((n - len(list(res.keys()))) * 2)
        return fams
