class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        a = 0
        b = 0
        coeff = ''
        right = 1
        for i in equation + '+':
            if (i == '+' or i == '-' or i == '=') and coeff != '':
                if 'x' in coeff:
                    coeff = coeff.strip('x')
                    if coeff == '-':
                        a -= right
                    elif coeff == '+' or coeff == '':
                        a += right
                    else:
                        a += (int(coeff.strip('x')) * right)
                else:
                    b -= (int(coeff) * right)
                coeff = i
                if i == '=':
                    right = -1
                    coeff = ''
            else:
                coeff += i
        if a == 0 and b == 0:
            return "Infinite solutions"
        elif a == 0:
            return "No solution"
        elif b == 0:
            return "x=0"
        else:
            return "x=" + str(int(b / a))
