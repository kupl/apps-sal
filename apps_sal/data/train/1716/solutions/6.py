import itertools as it


def equal_to_24(*numbers):
    for template in ['{0}{4}({1}{5}({2}{6}{3}))', '({0}{4}{1}){5}({2}{6}{3})', '(({0}{4}{1}){5}c{2}{6}{3}']:
        for x in it.permutations(numbers):
            for i in it.product('*/+-', repeat=3):
                expr = template.format(*x, *i)
                try:
                    if eval(expr) == 24:
                        return expr
                except ZeroDivisionError:
                    pass
    return "It's not possible!"
