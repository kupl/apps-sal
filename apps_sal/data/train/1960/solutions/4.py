class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        (data, result) = (list(range(1, m + 1)), [])
        for item in queries:
            idx = data.index(item)
            data = [data[idx]] + data[:idx] + (data[idx + 1:] if idx + 1 < len(data) else [])
            result.append(idx)
        return result
