class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        dict_ = {}
        for row in matrix:
            curr_tuple = tuple(row)
            dict_[curr_tuple] = 1 + dict_.get(curr_tuple, 0)
        visited = set()
        max_same = 0
        for row in matrix:
            curr_tuple = tuple(row)
            if curr_tuple in visited:
                continue
            visited.add(curr_tuple)
            inverse = [1] * len(row)
            for i in range(len(row)):
                if row[i]:
                    inverse[i] = 0
            curr_inv = tuple(inverse)
            visited.add(curr_inv)
            curr_sum = 0
            curr_sum = dict_[curr_tuple]
            if curr_inv in dict_:
                curr_sum += dict_[curr_inv]
            if curr_sum > max_same:
                max_same = curr_sum
        return max_same
