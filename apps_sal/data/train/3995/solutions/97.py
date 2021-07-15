def dating_range(age):
    if age <= 14:
        min1 = age - .10 * age
        max1 = age + .10 * age
        min2 = int(min1)
        max2 = int(max1)
        return str(min2) + "-" + str(max2)
    if age > 14:
        min = age // 2 + 7
        max = (age - 7) * 2
        return str(min) + "-" + str(max)
