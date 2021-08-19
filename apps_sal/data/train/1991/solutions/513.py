class Solution:

    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        record = [[0] * (fuel + 1) for i in range(len(locations))]
        record[start][0] = 1
        count = 0
        for j in range(fuel + 1):
            for i in range(len(locations)):
                for c in range(len(locations)):
                    if c != i and j >= abs(locations[c] - locations[i]):
                        record[i][j] += record[c][j - abs(locations[c] - locations[i])]
                if i == finish:
                    count += record[i][j]
        return count % (10 ** 9 + 7)
