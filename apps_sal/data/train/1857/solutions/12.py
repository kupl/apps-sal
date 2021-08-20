class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        processed = {}
        seatdict = defaultdict(int)
        for i in reservedSeats:
            seatdict[i[0] - 1] += 2 ** i[1]
        counter = 0
        for i in seatdict:
            seatint = seatdict[i]
            if seatint in processed:
                counter += processed[seatint]
                continue
            else:
                subcounter = 0
                if seatint & 2 ** 4 + 2 ** 5 + 2 ** 6 + 2 ** 7 == 0:
                    subcounter += 1
                    if seatint & 2 ** 2 + 2 ** 3 + 2 ** 8 + 2 ** 9 == 0:
                        subcounter += 1
                elif seatint & 2 ** 2 + 2 ** 3 + 2 ** 4 + 2 ** 5 == 0:
                    subcounter += 1
                elif seatint & 2 ** 6 + 2 ** 7 + 2 ** 8 + 2 ** 9 == 0:
                    subcounter += 1
                processed[seatint] = subcounter
                counter += subcounter
        counter += 2 * (n - len(seatdict))
        return counter
