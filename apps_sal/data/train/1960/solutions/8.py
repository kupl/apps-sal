class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        permutations = [permutation for permutation in range(1, m + 1)]

        result = []
        for query in queries:
            for pindex, permutation in enumerate(permutations):
                if permutation == query:
                    result.append(pindex)
                    del permutations[pindex]
                    permutations.insert(0, permutation)
                    break
        print(result)
        print(permutations)
        
        return result

