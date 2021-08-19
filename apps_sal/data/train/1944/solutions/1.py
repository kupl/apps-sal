class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left_x = right_x = 0
        left_const = right_const = 0

        cur_left = True
        cur_num = 0
        cur_sign = 1
        has_num = False
        for c in equation:
            if c == "=":
                left_const += cur_num * cur_sign
                cur_num = 0
                cur_sign = 1
                cur_left = False
                has_num = False
            elif c in '+-':
                if cur_left:
                    left_const += cur_num * cur_sign
                else:
                    right_const += cur_num * cur_sign
                cur_num = 0
                cur_sign = 1 if c == '+' else -1
                has_num = False
            elif c == 'x':
                if cur_left:
                    left_x += cur_sign * (cur_num if has_num else 1)
                else:
                    right_x += cur_sign * (cur_num if has_num else 1)
                cur_num = 0
                has_num = False
            else:
                cur_num = cur_num * 10 + int(c)
                has_num = True

            # print(left_x, right_x, left_const, right_const, cur_num, cur_sign)

        right_const += cur_num * cur_sign
        left_x -= right_x
        right_const -= left_const

        if left_x == 0 and right_const == 0:
            return "Infinite solutions"
        elif left_x == 0 and right_const != 0:
            return "No solution"
        else:
            return "x=" + str(int(right_const / left_x))
