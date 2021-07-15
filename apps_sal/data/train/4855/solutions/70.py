from typing import Callable


def vert_mirror(strng: str) -> str:
    return '\n'.join(s[::-1] for s in strng.splitlines())


def hor_mirror(strng: str) -> str:
    return '\n'.join(strng.splitlines()[::-1])


def oper(fct: Callable[[str], str], s) -> str:
    return fct(s)

