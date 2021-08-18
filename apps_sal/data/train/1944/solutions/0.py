class Solution:
    def calc(self, part):
        part += "+"
        start = x = n = 0
        coeff = 1
        for end, char in enumerate(part):
            if char == "+" or char == "-":
                var = part[start:end]
                if var == "":
                    continue
                if "x" in var:
                    var = var[:-1]
                    if var in ["", "+"]:
                        var = 1
                    elif var == "-":
                        var = -1
                    x += int(var) * coeff
                    start = end
                else:
                    n += int(var) * coeff
                    start = end
        return x, n

    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """

        left, right = equation.split("=")
        x1, n1 = self.calc(left)
        x2, n2 = self.calc(right)
        x, n = x1 - x2, n1 - n2
        n = n / x if (x != 0) else n
        x = 1 if (x != 0) else x
        if x == 0 and n != 0:
            return "No solution"
        if x == 0 and n == 0:
            return "Infinite solutions"
        return "x={}".format(int(-n))
