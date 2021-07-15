class Nonogram:
      
    def __init__(self, clues):
        self.size, self.colclues, self.rowclues = 5, clues[0], clues[1]
        self.answer = [ [None] * self.size for _ in range(self.size) ]
        
    def possibilities(self):   
        from itertools import combinations

        colposs = []
        for clue in self.colclues:
            a = self.size - sum(clue) + 1
            b = len(clue)
            c = list(combinations(range(a),b))
            d = []
            for block in clue[:-1]:
                d.append([1]*block + [0])
            d.append([1]*clue[-1])     
            colcombs = []
            for thing in c:
                combblock = []
                e = d[:]
                for i in range(a):
                    if i in thing:
                        combblock.append(e.pop(0))
                    else:
                        combblock.append([0])
                comb = tuple([j for sublist in combblock for j in sublist])
                colcombs.append(comb)
            colposs.append(colcombs)        
            
        rowposs = []
        for clue in self.rowclues:
            a = self.size - sum(clue) + 1
            b = len(clue)
            c = list(combinations(range(a),b))
            d = []
            for block in clue[:-1]:
                d.append([1]*block + [0])
            d.append([1]*clue[-1])     
            rowcombs = []
            for thing in c:
                combblock = []
                e = d[:]
                for i in range(a):
                    if i in thing:
                        combblock.append(e.pop(0))
                    else:
                        combblock.append([0])
                comb = tuple([j for sublist in combblock for j in sublist])
                rowcombs.append(comb)
            rowposs.append(rowcombs)               
        return [colposs,rowposs]

    def colfill(self):
        for i in range(self.size):
            for j in range(self.size):
                allOne = True
                allZero = True
                for poss in self.colposs[i]:
                    if poss[j] == 1:
                        allZero = False
                    else:
                        allOne = False
                if allOne:
                    self.answer[j][i] = 1
                elif allZero:
                    self.answer[j][i] = 0

    def rowfill(self):
        for i in range(self.size):
            for j in range(self.size):
                allOne = True
                allZero = True
                for poss in self.rowposs[i]:
                    if poss[j] == 1:
                        allZero = False
                    else:
                        allOne = False
                if allOne:
                    self.answer[i][j] = 1
                elif allZero:
                    self.answer[i][j] = 0  
    
    def colelim(self):
        for i in range(self.size):
            for poss in reversed(self.colposs[i]):
                for j in range(self.size):
                    if (not self.answer[j][i] is None) and self.answer[j][i] != poss[j]:
                        self.colposs[i].remove(poss)
                        break
    
    def rowelim(self):
        for i in range(self.size):
            for poss in reversed(self.rowposs[i]):
                for j in range(self.size):
                    if (not self.answer[i][j] is None) and self.answer[i][j] != poss[j]:
                        self.rowposs[i].remove(poss)
                        break
    
    def isSolved(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.answer[i][j] is None:
                    return False
        return True        
    
    def solve(self):
        from itertools import chain
        poss = self.possibilities()
        self.colposs, self.rowposs = poss[0], poss[1]   
        while not self.isSolved():
            self.colfill()
            self.rowelim()
            self.rowfill()
            self.colelim()
            
        return tuple([tuple(row) for row in self.answer])
