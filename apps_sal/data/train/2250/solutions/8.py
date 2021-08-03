

"""
NTC here
"""
import sys
inp = sys.stdin.readline
def input(): return inp().strip()
# flush= sys.stdout.flush
# import threading
# sys.setrecursionlimit(10**6)
# threading.stack_size(2**26)


def iin(): return int(input())


def lin(): return list(map(int, input().split()))


# range = xrange
# input = raw_input


def main():

    T = 1

    def fn(ch, x, y):
        return x * ch[0] + y * ch[1] + ch[2] == 0

    def fnx(ch, y):
        return (-ch[1] * y - ch[2]) / ch[0]

    def fny(ch, x):
        return (-ch[0] * x - ch[2]) / ch[1]

    def int_val(x):
        return int(x * 10000) == int(x) * 10000
    while T:
        T -= 1
        n, m, k = lin()
        h = m
        w = n
        end = {(0, h), (0, 0), (w, h), (w, 0)}
        sensors = [lin() for _ in range(k)]
        # we will track ray
        # as line as set of ax+by+c=0
        lines = {(1, -1, 0): [(0, 0), 0]}
        ch = [1, -1, 0]
        ch1 = 1
        ch2 = 0
        st = [0, 0]
        while 1:
            # print('EQ-', ch)
            # print(st)
            dn = 0
            # y = h
            y1 = h
            x1 = fnx(ch, y1)
            # print("D",[x1, y1])
            if int_val(x1) and 0 <= int(x1) <= w and [int(x1), int(y1)] != st:
                x1 = int(x1)
                if x1 == w:
                    break
                dn = 1
            # y = 0
            if dn == 0:
                y1 = 0
                x1 = fnx(ch, 0)
                # print("A",[x1, y1])
                if int_val(x1) and 0 <= int(x1) <= w and [int(x1), int(y1)] != st:
                    x1 = int(x1)
                    if x1 == 0:
                        break
                    dn = 1

                if dn == 0:
                    # x = 0
                    x1 = 0
                    y1 = fny(ch, x1)
                    # print("B",[x1, y1])
                    if int_val(y1) and 0 <= int(y1) <= h and [int(x1), int(y1)] != st:
                        y1 = int(y1)
                        if y1 == 0:
                            break
                        dn = 1

                    if dn == 0:
                        # x = w
                        x1 = w
                        y1 = fny(ch, x1)
                        # print("C",[x1, y1])
                        if int_val(y1) and 0 <= int(y1) <= h and [int(x1), int(y1)] != st:
                            y1 = int(y1)
                            if y1 == h:
                                break
                            dn = 1
            if dn:

                # print(x1, y1)
                ch2 += abs(st[0] - x1)
                ch1 = -1 if ch1 == 1 else 1
                ch = [ch1, -1, -ch1 * x1 + y1]
                if tuple(ch) in lines:
                    continue
                lines[tuple(ch)] = [[x1, y1], ch2]
                if (x1, y1) in end:
                    break

                st = [x1, y1]
            else:
                break
        # print(lines)
        for i, j in sensors:
            ch1, ch2 = (1, -1, -i + j), (-1, -1, i + j)
            # print((i, j), ch1, ch2)
            ans = -1
            if ch1 in lines:
                p, c1 = lines[ch1]
                ans = abs(p[0] - i) + c1
            if ch2 in lines:
                p, c1 = lines[ch2]
                ans = abs(p[0] - i) + c1 if ans == -1 else min(abs(p[0] - i) + c1, ans)
            print(ans)


main()

# threading.Thread(target=main).start()
