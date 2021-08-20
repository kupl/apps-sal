def solution(items, index, default_value):
    print((items, index, default_value))
    if index >= -len(items) and index < len(items):
        return items[index]
    else:
        return default_value
