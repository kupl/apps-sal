class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        areas = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele == '.':
                    continue
                area_id = i // 3 * 3 + j // 3
                if ele in rows[i] or ele in cols[j] or ele in areas[area_id]:
                    return False
                else:
                    rows[i].append(ele)
                    cols[j].append(ele)
                    areas[area_id].append(ele)
        return True
