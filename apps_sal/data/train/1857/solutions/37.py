class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_in_row = defaultdict(list)
        for i, j in reservedSeats:
            reserved_in_row[i].append(j)
        res = 2 * (n - len(reserved_in_row))
        for i in reserved_in_row:
            sim = [0 for _ in range(10)]
            for j in reserved_in_row[i]:
                sim[j - 1] = 1
            temp_res = res
            if sim[1: 5] == [0 for _ in range(4)]:
                res += 1
            if sim[5: 9] == [0 for _ in range(4)]:
                res += 1
            if res == temp_res and sim[3: 7] == [0 for _ in range(4)]:
                res += 1
        return res
