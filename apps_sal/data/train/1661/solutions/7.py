from collections import deque
import re
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3
DIRECTIONS = [Point(1, 0), Point(0, -1), Point(-1, 0), Point(0, 1)]
FORWARD = 1
BACKWARD = -1


def generate_jump_map(code):
    jump_map = {}
    opening_bracket_stack = deque()
    for (i, c) in enumerate(code):
        if c == '(':
            opening_bracket_stack.append(i)
        elif c == ')':
            opening_index = opening_bracket_stack.pop()
            jump_map[i] = opening_index
            jump_map[opening_index] = i
    return jump_map


execution_count_pattern = re.compile('\\d*')


def code_unwrap(code):
    jump_map = generate_jump_map(code)

    def code_unwrap_inner(code, ip, end_address):
        while ip < end_address:
            execution_count_str = execution_count_pattern.match(code[ip + 1:]).group(0)
            execution_count = int(execution_count_str or '1')
            for _ in range(execution_count):
                if code[ip] == ')':
                    yield from code_unwrap_inner(code, jump_map[ip] + 1, ip)
                elif code[ip] == '(':
                    ip = jump_map[ip] - 1
                else:
                    yield code[ip]
            ip += 1 + len(execution_count_str)
    yield from code_unwrap_inner(code, 0, len(code))


def execute(code):
    visited = {Point(0, 0)}
    pos = Point(0, 0)
    direction = RIGHT

    def get_area():
        xmin = 2 ** 30
        xmax = -2 ** 30
        ymin = 2 ** 30
        ymax = -2 ** 30
        for (x, y) in visited:
            xmin = min(xmin, x)
            xmax = max(xmax, x)
            ymin = min(ymin, y)
            ymax = max(ymax, y)
        return (xmin, xmax, ymin, ymax)
    for c in code_unwrap(code):
        if c == 'F':
            delta = DIRECTIONS[direction]
            pos = Point(pos.x + delta.x, pos.y + delta.y)
            visited.add(pos)
        elif c == 'L':
            direction = (direction + 1) % 4
        elif c == 'R':
            direction = (direction - 1) % 4
    (xmin, xmax, ymin, ymax) = get_area()
    ret = '\r\n'.join((''.join(('*' if (x, y) in visited else ' ' for x in range(xmin, xmax + 1))) for y in range(ymin, ymax + 1)))
    return ret
