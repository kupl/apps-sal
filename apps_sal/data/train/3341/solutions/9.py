def pop_shift(str):
    l = len(str)
    return [str[::-1][:l//2], str[:l//2], str[l//2]*(l%2)]
