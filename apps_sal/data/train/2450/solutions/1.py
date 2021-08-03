class Solution:
    def average(self, salary: List[int]) -> float:
        mx = 0
        mn = 100005
        sm = 0
        n = len(salary) - 2
        for i in salary:
            if i > mx:
                mx = i
            if i < mn:
                mn = i
        print((mn, mx))
        return (sum(salary) - (mn + mx)) / n
