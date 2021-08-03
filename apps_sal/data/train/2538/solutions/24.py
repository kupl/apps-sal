class Solution:
    def countLargestGroup(self, n: int) -> int:
        print(n)
        str_nums = [str(i) for i in range(1, n + 1)]
        print(str_nums)
        digits = [[int(i) for i in s] for s in str_nums]
        print(digits)
        sums = [sum(i) for i in digits]
        print(sums)
        group_sizes = {}
        for s in sums:
            group_sizes[s] = group_sizes.get(s, 0) + 1
        max_size = max(group_sizes.values())
        return len([i for i in group_sizes if group_sizes[i] == max_size])
