class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        seen = defaultdict(int)

        for row in matrix:
            comp = row[0] == 1

            temp = []

            for num in row:
                if comp:
                    temp.append(str(num ^ 1))
                else:
                    temp.append(str(num))

            seen[''.join(temp)] += 1

        return max(seen.values())
