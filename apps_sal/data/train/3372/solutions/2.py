def string_merge(s1: str, s2: str, letter: str) -> str:
    return f"{s1.partition(letter)[0]}{letter}{s2.partition(letter)[2]}"

