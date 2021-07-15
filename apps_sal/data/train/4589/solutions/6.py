def solution(items: list, index: int, default_value):
    try:
        return items[index]
    except IndexError:
        return default_value

