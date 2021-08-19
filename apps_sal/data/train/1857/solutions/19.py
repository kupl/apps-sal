class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        dicts = collections.defaultdict(list)
        for r in reservedSeats:
            dicts[r[0]].append(r[1])
        res = 0
        res += 2 * (n - len(dicts))
        for k in list(dicts.keys()):
            left = True
            right = True
            middle = True
            for seat in dicts[k]:
                if 2 <= seat and seat <= 3 or (seat >= 4 and seat <= 5):
                    left = False
                if seat >= 8 and seat <= 9 or (seat >= 6 and seat <= 7):
                    right = False
                if seat >= 4 and seat <= 7:
                    middle = False
            if left and right and middle:
                res += 2
            elif left or right or middle:
                res += 1
        return res
