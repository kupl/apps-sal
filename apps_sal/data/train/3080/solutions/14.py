def who_is_paying(name):
    return [name, name[0] + name[1]] if len(name) > 2 else [name]
    # Program returns name and then the first two letters in the string provided IF the length of the string is over 2.
    # Otherwise it will only print the name
