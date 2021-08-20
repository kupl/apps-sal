class Solution:

    def average(self, salary: List[int]) -> float:
        minSalary = min(salary)
        maxSalary = max(salary)
        total = sum(salary)
        return (total - minSalary - maxSalary) / (len(salary) - 2)
