def solution(items, index, default_value):
    return items[index] if abs(index + .5) < len(items) + .5 else default_value
