class Solution:

    def average(self, salary: List[int]) -> float:
        minSalary = None
        maxSalary = None
        s = 0
        for n in salary:
            s = s + n
            if minSalary is None or n < minSalary:
                minSalary = n
            if maxSalary is None or n > maxSalary:
                maxSalary = n
        return (s - minSalary - maxSalary) * 1.0 / (len(salary) - 2)
