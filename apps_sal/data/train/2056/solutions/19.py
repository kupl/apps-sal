import atexit
import io
import sys
inf = float('inf')
inf_neg = float('-inf')
range_5 = int(100000.0 + 1)
range_6 = int(1000000.0 + 1)
range_7 = int(10000000.0 + 1)
range_8 = int(100000000.0 + 1)
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


def main():
    n = int(input())
    a = list(input())
    b = list(input())
    ret = 0
    for i in range(n - 1):
        if a[i] == '0' and b[i] == '1' and (a[i + 1] == '1') and (b[i + 1] == '0'):
            (a[i], a[i + 1]) = (a[i + 1], a[i])
            ret += 1
        elif a[i] == '1' and b[i] == '0' and (a[i + 1] == '0') and (b[i + 1] == '1'):
            (a[i], a[i + 1]) = (a[i + 1], a[i])
            ret += 1
    for i in range(n):
        if a[i] != b[i]:
            ret += 1
    print(ret)


def __starting_point():
    main()


__starting_point()
