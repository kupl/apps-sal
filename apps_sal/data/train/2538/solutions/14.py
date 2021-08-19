class Solution:

    def countLargestGroup(self, n: int) -> int:
        sum_to_nums = {}
        for i in range(1, n + 1):
            digit_sum = self.getDigitSum(i)
            if digit_sum in sum_to_nums:
                sum_to_nums[digit_sum].append(i)
            else:
                sum_to_nums[digit_sum] = [i]
        print(sum_to_nums)
        values = list(sum_to_nums.values())
        num_values = list([len(v) for v in values])
        largest_group = max(num_values)
        print(num_values)
        summing = [1 if x == largest_group else 0 for x in num_values]
        print(summing)
        return sum(summing)

    def getDigitSum(self, num):
        sum_so_far = 0
        while num != 0:
            digit = num % 10
            sum_so_far = sum_so_far + digit
            num = int(num / 10)
        return sum_so_far
