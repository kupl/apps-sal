# class Solution:
#     def average(self, salary: List[int]) -> float:
#         maxs = 0
#         mins = 10000000 
#         sums = 0 
#         for s in salary:
#             sums += s
#             maxs = max(maxs, s)
#             mins = min(mins, s)
#         return (sums -maxs -mins) / (len(salary) - 2)  # 用// 错
            
# ###用python内置函数快一点
# class Solution:
#     def average(self, salary: List[int]) -> float:
#         maxs = max(salary)
#         mins = min(salary) 
#         sums = sum(salary)
#         return (sums -maxs -mins) / (len(salary) - 2)  # 用// 错
    
#copy other
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        del salary[0]
        del salary[-1]
        return sum(salary)/len(salary)
