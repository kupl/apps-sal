class Solution:

    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        rows = [1]
        for i in range(1, len(board)):
            num = self.get_num(board[0], board[i])
            if 0 <= num <= 1:
                rows.append(num)
            else:
                return -1
        r1 = self.swap_count(rows)
        if r1 != -1:
            r2 = self.swap_count(board[0])
        if r1 == -1 or r2 == -1:
            return -1
        else:
            return r1 + r2

    def get_num(self, r1, r2):
        eq = True
        op = True
        for i in range(len(r1)):
            if r1[i] == r2[i]:
                op = False
            else:
                eq = False
        if eq:
            return 1
        elif op:
            return 0
        else:
            return -1

    def swap_count(self, bits):
        n = len(bits)
        ones = sum(bits)
        zeros = n - ones
        ones_in_even = 0
        zeros_in_even = 0
        for i in range(0, n, 2):
            ones_in_even += bits[i]
            zeros_in_even += 1 - bits[i]
        if abs(ones - zeros) > 1:
            return -1
        if n % 2 == 0:
            return min(zeros_in_even, ones_in_even)
        elif ones > zeros:
            return zeros_in_even
        else:
            return ones_in_even
