from typing import List, Tuple


def solution(args: List[int]) -> str:
    res: str = ""
    length: int = len(args)
    idx: int = 0

    while idx < length:
        if isRange(args, idx):
            r, inc = showRange(args, idx)
            res += r
            idx += inc
        else:
            r = showInt(args, idx)  # handles separator
            res += r
            idx += 1
    return res


def isRange(rng: List[int], idx: int) -> bool:
    # a range spans at least 3 integers
    if len(rng)-3 < idx:
        return False

    n: int = rng[idx]
    nn: int = rng[idx+1]
    nnn: int = rng[idx+2]
    if n+1 == nn and nn+1 == nnn:
        return True

    return False


def showRange(rng: List[int], idx: int) -> Tuple[str, int]:
    # determine range
    # determine if range spans until the end (for separator!)
    curr: int = idx
    length: int = len(rng)
    while rng[curr]+1 == rng[curr+1]:
        curr += 1
        if (curr+1 == length):
            break

    res: str = str(rng[idx]) + "-" + str(rng[curr])
    dist: int = curr - idx + 1
    assert(dist >= 3)  # implied by the algorithm
    if not atEnd(rng, curr):
        res += ","

    return (res, dist)


def showInt(rng: List[int], idx: int) -> str:
    res: str = str(rng[idx])
    if atEnd(rng, idx):
        return res
    else:
        return res + ","


def atEnd(lst: List, idx: int) -> bool:
    return len(lst)-1 == idx
