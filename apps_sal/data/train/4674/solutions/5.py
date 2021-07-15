from typing import List


def rank(st: str, we: List[int], n: int):
    if not st:
        return "No participants"

    names = st.split(',')
    if n > len(names):
        return "Not enough participants"

    return sorted(((-w * (len(s) + sum(ord(c) - 96 for c in s.lower())), s) for s, w in zip(names, we)))[n - 1][1]

