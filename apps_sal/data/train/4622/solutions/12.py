def double_check(s):
    return any(prev_val.lower() == next_val.lower() for prev_val, next_val in zip(s, s[1:]))
