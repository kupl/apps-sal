def who_is_paying(name):
    var = []
    if len(name) <= 2:
        var.append(name)
        return var
    var.append(name)
    var.append(name[0] + name[1])
    return var
