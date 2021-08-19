import itertools as it


def equal_to_24(*numbers):
    for template in ['aZ(bX(cVd))', '(aZb)X(cVd)', '((aZb)Xc)Vd']:
        for x in it.permutations(numbers):
            for i in it.product('*/+-', repeat=3):
                temp = template
                for r in (('Z', i[0]), ('X', i[1]), ('V', i[2]), ('a', str(x[0])), ('b', str(x[1])), ('c', str(x[2])), ('d', str(x[3]))):
                    temp = temp.replace(*r)
                try:
                    if eval(temp) == 24:
                        return temp
                except ZeroDivisionError:
                    pass
    return "It's not possible!"
