import re


def count_squares(lines):
    h, w = len(lines), max(map(len, lines))
    grid = "\t".join(line.ljust(w) for line in lines)

    return sum(
        len(re.findall(r"(?=\+[-+]{%d}\+.{%d}(?:[|+].{%d}[|+].{%d}){%d}\+[-+]{%d}\+)"
                       % (i, w + 1 - i - 2, i, w + 1 - i - 2, i, i), grid))
        for i in range(0, min(w, h) - 1)
    )
