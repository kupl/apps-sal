from collections import defaultdict


def interpreter(tape):
    cells, cur, output = defaultdict(int), 0, ""
    for c in tape:
        if c == ">":
            cur += 1
        elif c == "<":
            cur -= 1
        elif c == "+":
            cells[cur] += 1
        elif c == "*":
            output = f"{output}{chr(cells[cur] % 256)}"
    return output

