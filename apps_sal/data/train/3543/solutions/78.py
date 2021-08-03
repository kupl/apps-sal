def increment_string(strng):
    originalnum = ''
    for t in reversed(strng):
        if not t.isdigit():
            break
        originalnum = t + originalnum
    if len(originalnum) > 0:
        num = int(originalnum) + 1
    else:
        return strng + "1"
    if len(str(num)) < len(originalnum):
        numstr = str(num).zfill(len(originalnum))
    else:
        numstr = str(num)
    return strng[0:-len(originalnum)] + numstr
