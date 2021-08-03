def dating_range(age):
    if age <= 14:
        minage = int(age - 0.1 * age)
        maxage = int(age + 0.1 * age)
    else:
        minage = int(age / 2 + 7)
        maxage = int((age - 7) * 2)

    return f"{minage}-{maxage}"
