def solution(items, index, default_value):
    return items[index] if abs(index) <= len(items) else default_value
