def feast(beast: str, dish: str) -> bool:
    return True if dish.startswith(beast[0]) and dish.endswith(beast[-1]) else False
