class Calculator(object):

    def evaluate(self, in_string):
        what = str()
        lst = []
        count_par = 0
        index = 0
        while index < len(in_string):
            if in_string[index] == '(':
                count_par += 1
                flag_par = True
            elif in_string[index] == ')':
                count_par -= 1
            elif count_par == 0:
                if in_string[index] in ['+', '-']:
                    break
                elif in_string[index] in ['*', '/']:
                    if in_string[index + 1] == '(':
                        break
                    elif in_string[index + 1:].count('+') == 0 and in_string[index + 1:].count('-') == 0:
                        break
            index += 1
        if index == len(in_string):
            lst.append(in_string)
        else:
            temp1 = in_string[0:index]
            temp2 = in_string[index + 1:]
            what = in_string[index]
            if temp1[0] == '(':
                temp1 = temp1[1:-1]
            if temp2[0] == '(':
                temp2 = temp2[1:-1]
            if what == '-' and in_string[index + 1] != '(':
                temp2 = temp2.replace('-', 'x')
                temp2 = temp2.replace('+', '-')
                temp2 = temp2.replace('x', '+')
            lst.append(temp1)
            lst.append(temp2)
        if len(lst) == 1:
            return float(lst[0])
        else:
            L = self.evaluate(lst[0])
            R = self.evaluate(lst[1])
            if what == '+':
                return L + R
            elif what == '-':
                return L - R
            elif what == '*':
                return L * R
            elif what == '/':
                return L / R if R != 0 else 0


def index_numbers(a, b, c, d):
    lst = [a, b, c, d]
    for i in lst:
        lst1 = lst[:]
        lst1.remove(i)
        for j in lst1:
            lst2 = lst1[:]
            lst2.remove(j)
            for k in lst2:
                lst3 = lst2[:]
                lst3.remove(k)
                for l in lst3:
                    yield [i, j, k, l]


def index_symbols():
    lst = ['+', '-', '*', '/']
    for i in lst:
        for j in lst:
            for k in lst:
                yield [i, j, k]


CAL = Calculator()


def evaluate0(num, sym):
    expr = num[0] + sym[0] + num[1] + sym[1] + num[2] + sym[2] + num[3]
    return (CAL.evaluate(expr), expr)


def evaluate1(num, sym):
    expr = '(' + num[0] + sym[0] + num[1] + sym[1] + num[2] + ')' + sym[2] + num[3]
    return (CAL.evaluate(expr), expr)


def evaluate2(num, sym):
    expr = '(' + num[0] + sym[0] + num[1] + ')' + sym[1] + '(' + num[2] + sym[2] + num[3] + ')'
    return (CAL.evaluate(expr), expr)


def evaluate3(num, sym):
    expr = num[0] + sym[0] + '(' + num[1] + sym[1] + '(' + num[2] + sym[2] + num[3] + '))'
    return (CAL.evaluate(expr), expr)


def evaluate4(num, sym):
    expr = '((' + num[0] + sym[0] + num[1] + ')' + sym[1] + num[2] + ')' + sym[2] + num[3]
    return (CAL.evaluate(expr), expr)


def equal_to_24(a, b, c, d):
    for num in index_numbers(str(a), str(b), str(c), str(d)):
        for sym in index_symbols():
            (val, text) = evaluate0(num, sym)
            if val == 24:
                return text
            (val, text) = evaluate1(num, sym)
            if val == 24:
                return text
            (val, text) = evaluate2(num, sym)
            if val == 24:
                return text
            (val, text) = evaluate3(num, sym)
            if val == 24:
                return text
            (val, text) = evaluate4(num, sym)
            if val == 24:
                return text
    return "It's not possible!"
