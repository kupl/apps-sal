from typing import Tuple, Optional, Union, Any, List, Dict, Callable, Iterator
from enum import Enum, auto
import re

OptFunc = Optional[Callable[[], Any]]

instructions_pattern = re.compile(r'F+\d*|L+\d*|R+\d*')


class BufferedIterator:
    _iter: Iterator[str]
    _stack: List[str]

    def __init__(self, it: Iterator[str]):
        self._iter = it
        self._stack = []

    def __iter__(self):
        return self

    def __next__(self):
        if self._stack:
            return self._stack.pop()
        else:
            return next(self._iter)

    def push(self, s):
        self._stack.append(s)


class StringBuf:
    _text: str

    def __init__(self, s: Optional[str] = None):
        self._text = s or ''

    def __str__(self):
        return self._text

    def __repr__(self):
        return f'StringBuf({self._text!r})'

    def append(self, s: str):
        self._text += s

    def prepend(self, s: str):
        self._text = s + self._text

    def __getitem__(self, idx):
        return self._text[idx]

    def __setitem__(self, idx, value):
        if isinstance(idx, int):
            self._text = self._text[:idx] + value + self._text[(idx + len(value)):]


class Rotation(Enum):
    No = auto()
    Left = auto()
    Right = auto()

    def switch(self, right: OptFunc = None, left: OptFunc = None, none: OptFunc = None) -> Any:
        if self is self.Right:
            if right is not None:
                return right()
        elif self is self.Left:
            if left is not None:
                return left()
        elif self is self.No:
            if none is not None:
                return none()

        return None


class Direction(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3

    @staticmethod
    def from_num(count: int) -> 'Direction':
        return Direction((4 - (-count % 4)) % 4 if count < 0 else count % 4)

    def to_num(self) -> int:
        return self.value

    def switch(self, up: OptFunc = None, right: OptFunc = None, down: OptFunc = None, left: OptFunc = None) -> Any:
        if self is self.Up:
            if up is not None:
                return up()
        elif self is self.Right:
            if right is not None:
                return right()
        elif self is self.Down:
            if down is not None:
                return down()
        elif self is self.Left:
            if left is not None:
                return left()

        return None

    def next(self, pos: Tuple[int, int], count: int) -> Tuple[int, int]:
        return self.switch(
            up=lambda: (pos[0], pos[1] - count),
            right=lambda: (pos[0] + count, pos[1]),
            down=lambda: (pos[0], pos[1] + count),
            left=lambda: (pos[0] - count, pos[1]),
        )

    def change(self, rot: Rotation, count: int) -> 'Direction':
        return rot.switch(
            left=lambda: Direction.from_num(self.to_num() - count),
            right=lambda: Direction.from_num(self.to_num() + count),
            none=lambda: self,
        )


class TheGridForTron:
    _grid: List[StringBuf]
    _size: int
    _org: Tuple[int, int]
    _pos: Tuple[int, int]
    _dir: Direction

    def __init__(self):
        self._grid = [StringBuf('*')]
        self._size = 1
        self._org = (0, 0)
        self._pos = (0, 0)
        self._dir = Direction.Right

    def _grow(self):
        # Grow to left
        diff = self._org[0] - self._pos[0]
        if diff > 0:
            self._org = (self._pos[0], self._org[1])
            self._size += diff

            s = ' ' * diff

            for line in self._grid:
                line.prepend(s)

            return

        # Grow to up
        diff = self._org[1] - self._pos[1]
        if diff > 0:
            self._org = (self._org[0], self._pos[1])

            s = ' ' * self._size
            for _ in range(diff):
                self._grid.insert(0, StringBuf(s))

            return

        # Grow to right
        diff = self._pos[0] - (self._org[0] + self._size) + 1
        if diff > 0:
            s = ' ' * diff

            self._size += diff
            for line in self._grid:
                line.append(s)

            return

        # Grow to down
        diff = self._pos[1] - (self._org[1] + len(self._grid)) + 1
        if diff > 0:
            s = ' ' * self._size
            for _ in range(diff):
                self._grid.append(StringBuf(s))

    def _trace_path(self, old: Tuple[int, int]):
        def up():
            pos = self._pos[0] - self._org[0]
            org = self._org[1]

            for line in self._grid[(self._pos[1] - org):(old[1] - org)]:
                line[pos] = '*'

        def right():
            self._grid[self._pos[1] - self._org[1]][old[0] + 1 - self._org[0]] = '*' * (self._pos[0] - old[0])

        def down():
            pos = self._pos[0] - self._org[0]
            org = self._org[1]

            for line in self._grid[(old[1] + 1 - org):(self._pos[1] + 1 - org)]:
                line[pos] = '*'

        def left():
            self._grid[self._pos[1] - self._org[1]][self._pos[0] - self._org[0]] = '*' * (old[0] - self._pos[0])

        self._dir.switch(
            up=up,
            right=right,
            down=down,
            left=left,
        )

    def do_move(self, rot: Rotation, count: int):
        if rot is Rotation.No:
            old = self._pos

            self._pos = self._dir.next(self._pos, count)
            self._grow()
            self._trace_path(old)
        else:
            self._dir = self._dir.change(rot, count)

    def serialize(self) -> str:
        return '\r\n'.join(map(str, self._grid))


class Executor:
    _grid: TheGridForTron
    _actions: Dict[str, Callable[[int], Any]]

    def __init__(self, grid: TheGridForTron):
        self._grid = grid
        self._actions = {
            'F': lambda cnt: self._grid.do_move(Rotation.No, cnt),
            'L': lambda cnt: self._grid.do_move(Rotation.Left, cnt),
            'R': lambda cnt: self._grid.do_move(Rotation.Right, cnt),
        }

    def do_actions(self, code: str):
        for m in instructions_pattern.finditer(code):
            action, count = parse_instruction(m.group())

            self._actions.get(action, lambda _: None)(count)


def expand_code(code: BufferedIterator) -> str:
    res: str = ''
    sub_str: str = ''
    in_group: bool = False
    count: Union[None, int] = None

    for ch in code:
        if in_group:
            try:
                count = ((count or 0) * 10) + int(ch)
            except ValueError:
                code.push(ch)
                if count is not None:
                    sub_str *= count
                    count = None

                res += sub_str
                sub_str = ''
                in_group = False
        else:
            if ch == ')':
                break

            if ch == '(':
                sub_str = expand_code(code)
                in_group = True
                continue

            res += ch

    if sub_str:
        if count is not None:
            sub_str *= count

        res += sub_str

    return res


def parse_instruction(code: str) -> Tuple[str, int]:
    c = code[0]

    count = code.lstrip(c)
    n = len(code) - len(count)

    if count:
        n += int(count) - 1

    return c, n


def execute(code: str) -> str:
    grid = TheGridForTron()

    Executor(grid).do_actions(expand_code(BufferedIterator(iter(code))))

    return grid.serialize()

