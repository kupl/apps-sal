from math import ceil
t = int(input())
rangex1 = int(0)
rangex2 = int(0)
rangey1 = int(0)
rangey2 = int(0)
while t > 0:
    n = int(input())
    h = [int(0)] * 11
    m = [int(0)] * 11
    alt = int(-1)
    for i in range(0, n):
        a, b = input().split(" ")
        h[i] = int(a)
        m[i] = int(b)

    if n == 1:
        print('1')
        print('0 Inf')
    else:
        state = int(1)
        count = int(0)
        index = int(0)
        curtime = int(0)
        while True:
            state = 1
            alt = -1
            for i in range(1, n):
                if i == 1:
                    if h[i] > h[i - 1]:
                        alt = 1
                    elif h[i] < h[i - 1]:
                        alt = 0
                    else:
                        alt = 2
                        state = 0
                        break
                elif alt == 1:
                    if h[i] < h[i - 1]:
                        alt = 0
                    else:
                        state = 0
                        break
                else:
                    if h[i] > h[i - 1]:
                        alt = 1
                    else:
                        state = 0
                        break

            if state == 1:
                count += 1
                if index == 0:
                    rangex1 = int(curtime)
                else:
                    rangex2 = int(curtime)

            mintime = int(0)
            found = int(0)
            tt = int(0)
            for i in range(1, n):
                if h[i - 1] < h[i]:
                    if m[i - 1] > m[i]:
                        tt = int(ceil(float(h[i] - h[i - 1]) / float(m[i - 1] - m[i])))
                        if found == 0:
                            mintime = tt
                            found = 1
                        elif tt < mintime:
                            mintime = tt
                elif h[i - 1] > h[i]:
                    if m[i] > m[i - 1]:
                        tt = int(ceil(float(h[i - 1] - h[i]) / float(m[i] - m[i - 1])))
                        if found == 0:
                            mintime = tt
                            found = 1
                        elif tt < mintime:
                            mintime = tt
                else:
                    if m[i] != m[i - 1]:
                        tt = 1
                        if found == 0:
                            mintime = tt
                            found = 1
                        elif tt < mintime:
                            mintime = tt

            if found == 0:
                if state == 1:
                    if index == 0:
                        rangey1 = int(-1)
                        index += 1
                    else:
                        rangey2 = int(-1)
                        index += 1
                break
            else:
                if state == 1:
                    if index == 0:
                        rangey1 = int(curtime + mintime - 1)
                        index += 1
                    else:
                        rangey2 = int(curtime + mintime - 1)
                        index += 1

                curtime += mintime
                for i in range(0, n):
                    h[i] += m[i] * mintime

        if count > 1:
            if rangey1 == rangex2 - 1:
                rangey1 = rangey2
                count -= 1

        print(count)
        if count >= 1:
            if rangey1 == -1:
                print('%d Inf' % (rangex1))
            else:
                print(rangex1, rangey1)
        if count >= 2:
            if rangey2 == -1:
                print('%d Inf' % (rangex2))
            else:
                print(rangey1, rangey2)
    t -= 1
