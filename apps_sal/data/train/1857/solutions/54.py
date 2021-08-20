class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seated = defaultdict(set)
        for record in reservedSeats:
            seated.setdefault(record[0], set()).add(record[1])
        ans = 0
        ans += (n - len(seated)) * 2
        for i in seated:
            currentRow = seated[i]
            emptyLeft = 2 not in currentRow and 3 not in currentRow
            emptyMidLeft = 4 not in currentRow and 5 not in currentRow
            emptyMidRight = 6 not in currentRow and 7 not in currentRow
            emptyRight = 8 not in currentRow and 9 not in currentRow
            if emptyLeft and emptyMidLeft and emptyMidRight and emptyRight:
                ans += 2
            elif emptyLeft and emptyMidLeft:
                ans += 1
            elif emptyRight and emptyMidRight:
                ans += 1
            elif emptyMidLeft and emptyMidRight:
                ans += 1
        return ans
