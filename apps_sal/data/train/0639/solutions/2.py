# cook your dish here
from collections import Counter


def fib_str(s):
    count = Counter(s)
    if len(count) < 3:
        return True
    [a, b, c] = count.most_common(3)
    if a[1] == b[1] + c[1]:
        return True
    return False


def __starting_point():
    test = int(input())

    for _ in range(test):
        s = input()

        if fib_str(s):
            print("Dynamic")
        else:
            print("Not")


__starting_point()
