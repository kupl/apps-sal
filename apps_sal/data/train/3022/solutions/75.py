def two_highest(arg1):
    if type(arg1) is list:
        return [arg for arg in sorted(list(set(arg1)))[-1::-1][:2]]
