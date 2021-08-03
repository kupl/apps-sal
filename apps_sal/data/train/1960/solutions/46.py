class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        permutations = [permutation for permutation in range(1, m + 1)]

        result = []
        for qindex, query in enumerate(queries):
            for pindex, permutation in enumerate(permutations):
                if permutation == query:
                    result.append(pindex)
                    permutations = [permutation] + permutations[0:pindex] + permutations[pindex + 1:]
                    print(permutations)
                    break
        print(result)
        print(permutations)

        return result
