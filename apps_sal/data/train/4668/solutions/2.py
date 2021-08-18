def is_divisible_by_6(stg):
    result = []
    for d in "0123456789":
        r = int(d.join(stg.split("*")))
        if r % 6 == 0:
            result.append(str(r))
    return result
