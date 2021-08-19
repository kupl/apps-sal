li = [i for i in range(1000000) if '4' not in str(i) and '7' not in str(i) and (not i % 13)]


def unlucky_number(n):
    return next((len(li[:li.index(i)]) + 1 for i in range(n, -1, -1) if '4' not in str(i) and '7' not in str(i) and (not i % 13)))
