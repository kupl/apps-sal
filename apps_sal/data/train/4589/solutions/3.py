def solution(items, index, default_value):
    try:
        return items[index]
    except LookupError:
        return default_value

