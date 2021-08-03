def freq_seq(s, sep):
    freq = {}
    newStr = []
    for i in s:
        if freq.get(i) == None:
            freq[i] = 1
        else:
            freq[i] += 1
    for i in s:
        newStr.append(str(freq[i]))
    return sep.join(newStr)
