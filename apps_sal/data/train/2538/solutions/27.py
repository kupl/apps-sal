def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total


class Solution:

    def countLargestGroup(self, n: int) -> int:
        groups = {}
        for i in range(1, n + 1):
            s = sum_of_digits(i)
            groups[s] = groups.get(s, []) + [i]
        max_len = 0
        for lst in groups.values():
            max_len = max(max_len, len(lst))
        largest = 0
        for lst in groups.values():
            if len(lst) == max_len:
                largest += 1
        return largest
