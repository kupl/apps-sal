class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        [left, right] = equation.split('=')
        l = [0, 0]
        temp = ''
        flag = 1
        if left[0] == '-':
            flag = -1
            left = left[1:]
        for i in left:
            if i != '+' and i != '-':
                temp += i
            else:
                if temp[-1] != 'x':
                    l[1] += flag * int(temp)
                else:
                    if len(temp) == 1:
                        l[0] += flag
                    else:
                        l[0] += flag * int(temp[:-1])
                if i == '+':
                    flag = 1
                if i == '-':
                    flag = -1
                temp = ''
                print(l)
        if temp[-1] != 'x':
            l[1] += flag * int(temp)
        else:
            if len(temp) == 1:
                l[0] += flag
            else:
                l[0] += flag * int(temp[:-1])
        temp = ''
        r = [0, 0]
        flag = 1
        if right[0] == '-':
            flag = -1
            right = right[1:]
        for i in right:
            if i != '+' and i != '-':
                temp += i
            else:
                if temp[-1] != 'x':
                    r[1] += flag * int(temp)
                else:
                    if len(temp) == 1:
                        r[0] += flag
                    else:
                        r[0] += flag * int(temp[:-1])
                if i == '+':
                    flag = 1
                if i == '-':
                    flag = -1
                temp = ''
        if temp[-1] != 'x':
            r[1] += flag * int(temp)
        else:
            if len(temp) == 1:
                r[0] += flag
            else:
                r[0] += flag * int(temp[:-1])
        temp = ''
        print(l, r)
        if l[0] == r[0]:
            if l[1] == r[1]:
                return 'Infinite solutions'
            else:
                return 'No solution'
        else:
            ans = int((r[1] - l[1]) / (l[0] - r[0]))
            return 'x=' + str(ans)
