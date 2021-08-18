
from collections import OrderedDict


def __starting_point():
    num = int(input().strip())
    history = OrderedDict()

    for _ in range(num):
        word = str(input().strip().split())
        if word not in list(history.keys()):
            history[word] = 1
        else:
            history[word] += 1

    print((len(list(history.keys()))))
    print((" ".join(map(str, list(history.values())))))


__starting_point()
