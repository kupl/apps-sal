def look_and_say_and_sum(n):
    oldstr = "1"
    newstr = ""
    total = 1
    i = 1
    while (i < n):
        j = 0
        total = 0
        newstr = ""
        length = len(oldstr)
        while (j < length):
            look = oldstr[j]
            count = 0
            while (j < length and look == oldstr[j]):
                count += 1
                j += 1
            total += count
            total += int(look)
            newstr += str(count)
            newstr += look
        oldstr = newstr
        i += 1
    return (total)
