from collections import defaultdict
from bisect import bisect_left

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        answer = 0
        reserved = defaultdict(list)
        for row, col in reservedSeats:
            reserved[row].append(col)
        answer = (n - len(reserved)) * 2
        possibility = [[2, 5], [4, 7], [6, 9]]
        for reserved_seats in reserved.values():
            reserved_seats.sort()
            result = []
            for start, end in possibility:
                idx = bisect_left(reserved_seats, start)
                result.append(1) if idx == len(reserved_seats) or reserved_seats[idx] > end else result.append(0)
            answer += max(result[0] + result[2], result[1])
        return answer
