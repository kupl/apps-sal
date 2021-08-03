def repeat_str(repeat, string):
    return string + repeat_str(repeat - 1, string) if repeat else ''
