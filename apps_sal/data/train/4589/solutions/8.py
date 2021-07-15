def solution(items, index, default_value):
    return items[index] if abs(index + .5) + .5 <= len(items) else default_value
