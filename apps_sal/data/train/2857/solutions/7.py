def splitSentence(s):
    sum = ""
    result = []
    for i in s:
        if i == " ":
            result.append(sum)
            sum = ""
            continue
        sum = sum + i
    result.append(sum)

    return result

