from itertools import takewhile
from typing import List


def black_and_white(height: int, width: int, compressed: List[int]) -> List[List[int]]:
    def tracker():
        is_black = False
        line = 0
        for i in compressed:
            is_black = not is_black
            if line + i < width:
                yield i
                line += i
            else:
                yield width - line
                if is_black:
                    yield 0
                yield -1
                i -= width - line
                line = 0
                while i > width:
                    if is_black:
                        yield width
                        yield 0
                    else:
                        yield 0
                        yield width
                    yield -1
                    i -= width
                if i == 0 and is_black:
                    yield 0
                if i > 0:
                    if is_black:
                        yield i
                    else:
                        yield 0
                        yield i
                    line += i

    it = iter(tracker())
    return [[i for i in takewhile(lambda i: i >= 0, it)] for h in range(height)]
