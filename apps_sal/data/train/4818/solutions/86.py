def solution(a, b):
    if len(a) < len(b):
        short_str = a
        long_str = b
    else:
        short_str = b
        long_str = a
    
    return short_str + long_str + short_str

