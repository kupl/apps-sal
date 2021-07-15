def string_clean(s):
    temp = ""
    numbers = "1234567890"
    for i in s:
        if i in numbers:
            continue
        else:
            temp+=i
    return temp
