class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        newSalaryList = salary[1:-1]

        numSalaries = len(newSalaryList)

        return sum(newSalaryList) / numSalaries
