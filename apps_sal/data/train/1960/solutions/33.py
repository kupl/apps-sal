class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        result = []
        coord = [x for x in range(0, m)]
        for num in queries:
            before = coord[num - 1]
            result.append(before)
            coord = [x + 1 if x < before else x for x in coord]
            coord[num - 1] = 0
        return result
