def chmod_calculator(perm):
    perms = {"r": 4, "w": 2, "x": 1}
    value = ""
    for permission in ["user", "group", "other"]:
        value += str(sum(perms.get(x, 0) for x in perm.get(permission, "")))

    return value
