def correct(string: str) -> str:
    return string.translate(str.maketrans("501", "SOI"))

