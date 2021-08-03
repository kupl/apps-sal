import numpy as np
import pandas as pd


def tv_remote(word):
    print(word)
    screen = np.array([['a', 'b', 'c', 'd', 'e', '1', '2', '3'],
                       ['f', 'g', 'h', 'i', 'j', '4', '5', '6'],
                       ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
                       ['p', 'q', 'r', 's', 't', '.', '@', '0'],
                       ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']])

    screen_col = 0
    screen_row = 0
    start = screen[screen_row, screen_col]
    count = 0
    word = word
    lst = [x for x in word]

    for x in lst:
        if x in screen[screen_row]:
            result = np.where(screen == x)
            if result[1][0] > screen_col:
                count += (result[1][0] - screen_col) + 1
            elif result[1][0] < screen_col:
                count += (screen_col - result[1][0]) + 1
            else:
                count += 1
            screen_row = result[0][0]
            screen_col = result[1][0]

            print('Done with {}'.format(x))
            print(count)

        else:
            result = np.where(screen == x)
            if result[0][0] > screen_row:
                count += (result[0][0] - screen_row)
                if result[1][0] > screen_col:
                    count += (result[1][0] - screen_col) + 1
                elif result[1][0] < screen_col:
                    count += (screen_col - result[1][0]) + 1
                else:
                    count += 1

            elif result[0][0] < screen_row:
                count += (screen_row - result[0][0])
                if result[1][0] > screen_col:
                    count += (result[1][0] - screen_col) + 1
                elif result[1][0] < screen_col:
                    count += (screen_col - result[1][0]) + 1
                else:
                    count += 1

            screen_row = result[0][0]
            screen_col = result[1][0]
            print('Done with {}'.format(x))
            print(count)

    return count
