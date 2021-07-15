def solution(items, index, default_value):
    try:
        return items[index]
    except:
        return default_value
