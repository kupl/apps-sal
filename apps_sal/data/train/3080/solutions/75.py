# len(name) gives the number of characters in the string
def who_is_paying(name):
    if len(name) < 3:
        return [name]
    else:
        return [name, name[:2]]  # name[:2] gives the first two characters in string 'name'
