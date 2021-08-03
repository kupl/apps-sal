def is_divisible_by_6(stg):
    result = []
    for d in "0123456789":
        r = int(d.join(stg.split("*")))
        if r % 6 == 0:
            result.append(str(r))
    return result

# one-liner
#    return [str(int(stg.replace("*", d))) for d in "0123456789" if int(stg.replace("*", d)) % 6 == 0]
