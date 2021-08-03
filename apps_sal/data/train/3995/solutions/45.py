def dating_range(age):
    if age > 14:
        mn, mx = age // 2 + 7, (age - 7) * 2
    else:
        mn, mx = int(age * .9), int(age * 1.1)
    return f"{mn}-{mx}"
