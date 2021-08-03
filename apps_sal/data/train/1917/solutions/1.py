class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack = [collections.Counter()]

        i = 0
        length = len(formula)
        ss = ""
        while i < length:
            if formula[i].isupper():
                ss = formula[i]
                i += 1
                while i < length:
                    if formula[i].islower():
                        ss += formula[i]
                        i += 1
                    else:
                        i -= 1
                        break
                num = 0
                i += 1
                while i < length:
                    if formula[i].isdigit():
                        num = 10 * num + int(formula[i])
                        i += 1
                    else:
                        i -= 1
                        break
                num = num if num else 1
                stack[-1][ss] = num if ss not in stack[-1] else stack[-1][ss] + num

            elif formula[i] == "(":
                stack.append(collections.Counter())
            elif formula[i] == ")":
                i += 1
                multiplier = 0
                while i < length:
                    if formula[i].isdigit():
                        multiplier = 10 * multiplier + int(formula[i])
                        i += 1
                    else:
                        i -= 1
                        break
                cur = stack.pop()
                for n, v in list(cur.items()):
                    stack[-1][n] = stack[-1][n] + v * multiplier if n in stack[-1] else v * multiplier

            i += 1
        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                       for name in sorted(stack[-1]))
