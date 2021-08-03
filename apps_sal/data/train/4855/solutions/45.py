from typing import Callable


def oper(callback: Callable[[str], str], string: str) -> str:
    return callback(string)


def vert_mirror(string: str) -> str:
    return '\n'.join([
        line[::-1] for line in string.split('\n')
    ])


def hor_mirror(string: str) -> str:
    return '\n'.join(
        string.split('\n')[::-1]
    )
