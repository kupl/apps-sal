def find_digit(num: int, nth: int) -> int:
    if nth < 1:
        return -1
    try:
        return int(str(abs(num))[-nth])
    except IndexError:
        return 0


