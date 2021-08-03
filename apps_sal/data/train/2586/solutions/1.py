#!/usr/bin/env python3

import re


def __starting_point():
    string = input()
    sub = input()

    matches = list(re.finditer(r'(?={})'.format(sub), string))

    if matches:
        for match in matches:
            print((match.start(), match.end() + len(sub) - 1))
    else:
        print((-1, -1))


__starting_point()
