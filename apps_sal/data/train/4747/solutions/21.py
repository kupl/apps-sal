def repeat_str(repeat, string):
    return string if repeat is 1 else string + repeat_str(repeat - 1, string)
