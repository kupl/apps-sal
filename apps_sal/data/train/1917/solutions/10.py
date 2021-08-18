class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """

        stack = [collections.Counter()]
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                stack.append(collections.Counter())
                print('new stack', stack)
                i += 1
            elif formula[i] == ')':
                i += 1

                num_start = i

                while i < len(formula) and formula[i].isdigit():
                    i += 1

                mult = formula[num_start:i]

                if mult is '':
                    mult = 1
                else:
                    mult = int(formula[num_start:i])

                top = stack[-1]
                print('top: ', top)
                print('new mult: ', mult)
                stack.pop()
                print('poped top stack: ', stack)
                for name in top:
                    stack[-1][name] = stack[-1][name] + top[name] * mult
            else:
                name = formula[i]
                i += 1
                while i < len(formula) and formula[i].islower():
                    name += formula[i]
                    i += 1

                print('name of atom: ', name)

                num_start = i

                while i < len(formula) and formula[i].isdigit():
                    i += 1

                mult = formula[num_start:i]

                if mult is '':
                    mult = 1
                else:
                    mult = int(formula[num_start:i])

                print('mult of {}: '.format(name), mult)

                stack[-1][name] += mult
                print('updated current stack: ', stack)

        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                       for name in sorted(stack[-1]))
