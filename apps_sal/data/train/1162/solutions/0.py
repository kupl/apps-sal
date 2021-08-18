import sys
import os


def __starting_point():
    start = 0
    for line in sys.stdin:
        if start == 0:
            start = 1
            continue
        else:
            try:
                n = int(line.strip())

                q = n / 7
                rem = n % 7

                if rem == 0:
                    res = n
                elif rem == 1:
                    res = (q - 1) * 7
                elif rem == 2:
                    res = (q - 2) * 7
                elif rem == 3:
                    res = (q - 3) * 7
                elif rem == 4:
                    res = q * 7
                elif rem == 5:
                    res = (q - 1) * 7
                elif rem == 6:
                    res = (q - 2) * 7

                if res < 0:
                    print(-1)
                else:
                    print(res)

            except:
                break


__starting_point()
