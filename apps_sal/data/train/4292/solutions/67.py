def string_clean(s):
    return ''.join(['' if char.isdigit() else char for char in s])
