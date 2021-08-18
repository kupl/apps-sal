
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
