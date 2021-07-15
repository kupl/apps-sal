class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        permutation = {num: num-1 for num in range(1, m+1)}
        ans = []
        for query in queries:
            ans.append(permutation[query])
            pos = permutation[query]
            for key in permutation.keys():
                if permutation[key] < pos:
                    permutation[key] += 1
            permutation[query] = 0
        return ans
