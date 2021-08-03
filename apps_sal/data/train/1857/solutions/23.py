class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rowseats = defaultdict(list)
        for s in reservedSeats:
            rowseats[s[0]].append(s[1])

        subtract = 0
        for _, seats in rowseats.items():
            left = True
            right = True
            middle = True
            for s in seats:
                if 2 <= s <= 5:
                    left = False
                if 4 <= s <= 7:
                    middle = False
                if 6 <= s <= 9:
                    right = False
            if left and right:
                subtract += 0
            elif left or right or middle:
                subtract += 1
            else:
                subtract += 2

        return n * 2 - subtract
