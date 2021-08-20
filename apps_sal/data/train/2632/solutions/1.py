from collections import OrderedDict


def __starting_point():
    num = int(input().strip())
    history = OrderedDict()
    for _ in range(num):
        get_log = input().strip().split()
        good = ' '.join(get_log[:-1])
        sold = int(get_log[-1])
        if good not in list(history.keys()):
            history[good] = sold
        else:
            history[good] += sold
    for key in list(history.keys()):
        print('{} {}'.format(key, history[key]))


__starting_point()
