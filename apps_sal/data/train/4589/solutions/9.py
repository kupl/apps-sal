def solution(items, index, default_value):
    return items[index] if abs(index + 0.5) < len(items) + 0.5 else default_value
