def weight(s):
    return sum(int(char) for char in s), s


def order_weight(string):
    # your code
    lst = string.split()
    lst.sort(key=weight)
    return ' '.join(lst)
