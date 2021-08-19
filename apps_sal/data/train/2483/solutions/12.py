class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique = set(arr)
        sol = []
        for i in unique:
            sol.append(arr.count(i))
        print(sol)
        for i in sol:
            if sol.count(i) > 1:
                return False
        return True
