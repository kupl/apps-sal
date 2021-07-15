def strip_line(line, markers):
    for m in markers:
        if m in line:
            line = line[:line.index(m)]
    return line.rstrip()

def solution(string,markers):
    stripped = [strip_line(l, markers) for l in string.splitlines()]
    return '\n'.join(stripped)
