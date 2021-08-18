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
    a = sorted(a)
    b_el = sorted(b_el, key=lambda x: x.val)
    for i in range(0, n):
        b_el[i].asigned = a[n - 1 - i]
    b_el = sorted(b_el, key=lambda x: x.index)
    for i in b_el:
        print(i.asigned, end=' ')


main()
