from collections import Counter


def count_sel(lst):
    one = sum(float(i).is_integer() for i in lst)
    two = len(set(lst))
    three = sum(lst.count(i) == 1 for i in lst)
    four = [i for i in Counter(lst).most_common()]
    k = max(i[1] for i in four)
    four = sorted(i[0] for i in four if i[1] == k)
    five = lst.count(four[0])
    return [one, two, three, [four, five]]
