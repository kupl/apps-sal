def alan_annoying_kid(s):
    negative = False
    a = s.split()
    a[-1] = a[-1][:-1]
    if a[2] == "didn't":
        negative = True
    if not negative:
        return "I don't think you " + ' '.join(a[2:]) + " today, I think you didn't " + str(a[2][:-2]) + ' at all!'
    return "I don't think you didn't " + ' '.join(a[3:]) + ' today, I think you did ' + str(a[3]) + ' it!'
