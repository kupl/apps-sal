def solution(string, markers):
    lines = string.splitlines()
    for mark in markers:
        lines = [line.split(mark)[0].strip() for line in lines]
    return '\n'.join(lines)
