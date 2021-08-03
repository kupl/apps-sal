class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        d = {k: k + 1 for k in range(m)}
        result = []
        for q in queries:
            current_pos = self.findPos(d, q)
            result.append(current_pos)
            while current_pos > 0:
                d[current_pos] = d[current_pos - 1]
                current_pos -= 1
            d[0] = q
        return result

    def findPos(self, d, q):
        for idx, val in list(d.items()):
            if val == q:
                return idx
