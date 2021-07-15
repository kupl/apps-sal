#!/usr/bin/env python3

import re

def __starting_point():
    out = list(re.split('[.,]', input()))
    print("\n".join(filter(lambda x: re.match('[0-9]+',x), out)))
__starting_point()
