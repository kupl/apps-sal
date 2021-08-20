class Solution:
    lx = 0
    lc = 0
    rx = 0
    rc = 0

    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        self.lx = 0
        self.lc = 0
        self.rx = 0
        self.rc = 0
        size = len(equation)
        l = 0
        r = 0
        left = True
        for i in range(1, size):
            if equation[i] == '=':
                l = r
                r = i + 1
                self.lastEq(equation[l:r - 1], left)
                left = False
                continue
            if equation[i] in {'+', '-'}:
                if equation[r:i] in {'+', '-', ''}:
                    continue
                l = r
                r = i
                self.lastEq(equation[l:r], left)
            if i == size - 1:
                l = r
                r = i
                self.lastEq(equation[l:r + 1], left)
        x = self.lx - self.rx
        c = self.rc - self.lc
        if x == 0 and c == 0:
            return 'Infinite solutions'
        if x == 0:
            return 'No solution'
        return 'x=' + str(int(c / x))

    def lastEq(self, s, left):
        print(s)
        if 'x' in s:
            if s[0] != '-':
                if left:
                    if s in {'x', '+x'}:
                        self.lx += 1
                    else:
                        self.lx += float(s[:-1])
                elif s in {'x', '+x'}:
                    self.rx += 1
                else:
                    self.rx += float(s[:-1])
            elif left:
                if s in {'x', '-x'}:
                    self.lx -= 1
                else:
                    self.lx -= float(s[1:-1])
            elif s in {'x', '-x'}:
                self.rx -= 1
            else:
                self.rx -= float(s[1:-1])
        elif s[0] != '-':
            if left:
                self.lc += float(s)
            else:
                self.rc += float(s)
        elif left:
            self.lc -= float(s[1:])
        else:
            self.rc -= float(s[1:])
        print(str(self.lx) + 'x' + ' ' + str(self.lc) + ' = ' + str(self.rx) + 'x ' + str(self.rc))
