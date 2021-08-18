import re

DECIMAL_NUMBER_PATTERN = re.compile(r"[+-]?((\.\d+)|(\d+\.?\d*))")


def isDigit(string: str) -> bool:
    return DECIMAL_NUMBER_PATTERN.fullmatch(string) != None
