def who_is_paying(name):
    total = len(name)
    if total >= 3:
        first = name[0]
        second = name[1]
        first_two = first + second
        final = list([name,first_two])
        return final
    else:
        final = list([name])
        return final
