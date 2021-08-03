class Solution:
    def FindValid(self):
        a = "123456789"
        d, val = {}, {}
        for i in range(9):
            for j in range(9):
                temp = self.board[i][j]
                if temp != '.':
                    d[("r", i)] = d.get(("r", i), []) + [temp]
                    d[("c", j)] = d.get(("c", j), []) + [temp]
                    d[(i // 3, j // 3)] = d.get((i // 3, j // 3), []) + [temp]
                else:
                    val[(i, j)] = []
        for (i, j) in list(val.keys()):
            invalid = d.get(("r", i), []) + d.get(("c", j), []) + d.get((i // 3, j // 3), [])
            val[(i, j)] = [ele for ele in a if ele not in invalid]
        return val

    def CheckingSolution(self, ele, Pos, Updata):
        self.board[Pos[0]][Pos[1]] = ele
        del self.val[Pos]
        i, j = Pos
        for invalid in list(self.val.keys()):
            if ele in self.val[invalid]:
                if invalid[0] == i or invalid[1] == j or (invalid[0] // 3, invalid[1] // 3) == (i // 3, j // 3):
                    Updata[invalid] = ele
                    self.val[invalid].remove(ele)
                    if len(self.val[invalid]) == 0:
                        return False
        return True

    def Sudo(self, Pos, Updata):
        self.board[Pos[0]][Pos[1]] = "."
        for i in Updata:
            if i not in self.val:
                self.val[i] = Updata[i]
            else:
                self.val[i].append(Updata[i])

    def FindSolution(self):
        if len(self.val) == 0:
            return True
        Pos = min(list(self.val.keys()), key=lambda x: len(self.val[x]))
        nums = self.val[Pos]
        for ele in nums:
            updata = {Pos: self.val[Pos]}
            if self.CheckingSolution(ele, Pos, updata):
                if self.FindSolution():
                    return True
            self.Sudo(Pos, updata)
        return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.val = self.FindValid()
        self.FindSolution()
