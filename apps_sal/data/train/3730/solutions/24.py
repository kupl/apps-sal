def capitalize(s):
    Even = ''
    Odd = ''
    Result = []

    for i in range(len(s)):
        if i % 2 == 0:
            Even += s[i].upper()
        else:
            Even += s[i]
        if i % 2 != 0:
            Odd += s[i].upper()
        else:
            Odd += s[i]

    Result.append(Even)
    Result.append(Odd)

    return Result
