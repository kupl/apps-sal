class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.val = self.PossibleValue()
        self.Solver()

    def PossibleValue(self):
        nums = "123456789"
        d, val = {}, {}
        for i in range(9):
            for j in range(9):
                element = self.board[i][j]
                if element != ".":
                    d[("r", i)] = d.get(("r", i), []) + [element]
                    d[("c", j)] = d.get(("c", j), []) + [element]
                    d[(i // 3, j // 3)] = d.get((i // 3, j // 3), []) + [element]
                else:
                    val[(i, j)] = []
        for (i, j) in val.keys():
            temp = d.get(("r", i), []) + d.get(("c", j), []) + d.get((i // 3, j // 3), [])
            val[(i, j)] = [x for x in nums if x not in temp]
        return val

    def Solver(self):
        if len(self.val) == 0:
            return True
        kee = min(self.val.keys(), key=lambda x: len(self.val[x]))
        possible_nums = self.val[kee]
        #update = {}
        for n in possible_nums:
            update = {kee: self.val[kee]}
            if self.ValidOne(n, kee, update):
                if self.Solver():
                    return True
            # self.val[kee]=possible_nums
            self.undo(kee, update)
        return False

    def ValidOne(self, n, kee, update):
        self.board[kee[0]][kee[1]] = n
        del self.val[kee]
        i, j = kee
        for index in self.val:
            if (i == index[0] or j == index[1] or (i // 3, j // 3) == (index[0] // 3, index[1] // 3)) and (n in self.val[index]):
                update[index] = n
                self.val[index].remove(n)
                if len(self.val[index]) == 0:
                    return False
        return True

    def undo(self, kee, update):
        self.board[kee[0]][kee[1]] = "."
        for x in update:
            if x not in self.val:
                self.val[x] = update[x]
            else:
                self.val[x].append(update[x])
        return None
