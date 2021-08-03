def who_is_paying(name):
    # your code here
    if len(name) > 2:
        names = [name]
        names.append(name[:2])
        return names
    else:
        names = [name]
        return names
