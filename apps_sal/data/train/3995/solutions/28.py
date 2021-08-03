def dating_range(age):
    min_14 = str(int(age - 0.10 * age))
    max_14 = str(int(age + 0.10 * age))
    min = str(int(age / 2 + 7))
    max = str(int((age - 7) * 2))
    if age <= 14:
        return(min_14 + "-" + max_14)
    else:
        return (min + "-" + max)
