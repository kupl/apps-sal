# import atexit
# import io
# import sys
#
# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
# _OUTPUT_BUFFER = io.StringIO()
# sys.stdout = _OUTPUT_BUFFER
#
#
# @atexit.register
# def write():
#     sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

import bisect
from datetime import datetime


def main():
    n, m = list(map(int, input().split()))
    n -= 1

    timestamps = []
    raw = []
    while True:
        s = ""
        try:
            s = input()
        except:
            print(-1)
            return

        d = datetime.strptime(s[0:19], "%Y-%m-%d %H:%M:%S")
        timestamps.append(int(d.timestamp()))
        raw.append(s[0:19])
        idx = bisect.bisect_left(timestamps, timestamps[-1] - n)
        if len(timestamps) - idx == m:
            print(raw[-1])
            return


def __starting_point():
    main()

__starting_point()
