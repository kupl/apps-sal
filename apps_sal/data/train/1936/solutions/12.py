import math


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        req_length = math.ceil(math.log(label + 1, 2))
        curr_depth = req_length
        next_depth = curr_depth - 1
        res = []

        while len(res) != req_length - 1:

            res.insert(0, label)

            curr_numbers = list(range(2**(curr_depth - 1), 2**curr_depth))
            next_numbers = list(range(2**(next_depth - 1), 2**next_depth))

            if curr_depth % 2 == 0:
                curr_numbers.reverse()

            if next_depth % 2 == 0:
                next_numbers.reverse()

            # print(curr_numbers, next_numbers)

            label = next_numbers[curr_numbers.index(label) // 2]
            curr_depth -= 1
            next_depth -= 1
        res.insert(0, 1)
        return res
