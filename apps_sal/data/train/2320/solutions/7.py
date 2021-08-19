# http://codeforces.com/problemset/problem/840/A
class Element(object):
    def __init__(self, val, index, asigned=-1):
        self.val = val
        self.index = index
        self.asigned = asigned


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b_el = [Element(0, 0) for i in range(n)]

    for i in range(0, n):
        b_el[i].val = b[i]
        b_el[i].index = i
    # sort a by vals
    a = sorted(a)
    # sort b by vals
    b_el = sorted(b_el, key=lambda x: x.val)
    # asigna valores mayores a los menores
    for i in range(0, n):
        b_el[i].asigned = a[n - 1 - i]
    # reordenar b, esta vez por indices y print de valores asignados
    b_el = sorted(b_el, key=lambda x: x.index)
    for i in b_el:
        print(i.asigned, end=' ')


main()
