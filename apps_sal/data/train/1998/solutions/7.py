class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        q = collections.deque()
        steps = collections.defaultdict(int)

        start = tuple(board[0] + board[1])
        steps[start] = 0
        q.append(start)
        target = (1, 2, 3, 4, 5, 0)

        while q:
            bd = q.popleft()
            if bd == target:
                return steps[bd]
            ind = bd.index(0)
            i, j = ind // 3, ind % 3
            for m, n in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= m < 2 and 0 <= n < 3:
                    move = list(bd)
                    move[ind], move[m * 3 + n] = move[m * 3 + n], move[ind]
                    new_bd = tuple(move)
                    if new_bd not in steps or steps[new_bd] > steps[bd] + 1:
                        q.append(new_bd)
                        steps[new_bd] = steps[bd] + 1

        return -1
