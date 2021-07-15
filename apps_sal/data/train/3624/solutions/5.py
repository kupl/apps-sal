from itertools import count

def distribution_of_candy(a):
    for i in count():
        if all(x == a[0] for x in a):
            return [i, a[0]]
        a = [x + x % 2 for x in a]
        a = [(x + y) // 2 for x, y in zip(a, a[1:] + [a[0]])]
