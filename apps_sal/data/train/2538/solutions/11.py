class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}
        max = 0
        for i in range(1, n + 1):
            num_str = str(i)
            sum = 0
            for x in num_str:
                sum += int(x)
            if sum in groups:
                groups[sum].append(n)
            else:
                groups[sum] = [n]

            max = max if len(groups[sum]) < max else len(groups[sum])

        num_groups = 0
        for g in groups:
            if len(groups[g]) == max:
                num_groups += 1

        return num_groups
