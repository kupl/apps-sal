#!/usr/bin/env python3

import re

try:
    while True:
        s = input()
        m = re.search(r"[^a]", s)
        if m is None:
            print(s[:-1], end="z\n")
        else:
            j = s.find('a', m.end())
            if j == -1:
                j = len(s)
            print(end=s[:m.start()])
            for i in range(m.start(), j):
                print(end=chr((ord(s[i]) - 98) % 26 + 97))
            print(s[j:])

except EOFError:
    pass
