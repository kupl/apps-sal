class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = [i - 1 for i in range(0, m + 1)]
        res = []
        for i in range(0, len(queries)):
            res.append(arr[queries[i]])
            for j in range(1, m + 1):
                if arr[j] < arr[queries[i]]:
                    arr[j] += 1
            arr[queries[i]] = 0
        return res
