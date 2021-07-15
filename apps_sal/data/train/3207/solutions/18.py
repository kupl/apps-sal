def reverseWords(str):
    liststr = str.split()
    liststr.reverse()
    newstr = ''
    for i in range(len(liststr)):
        newstr += liststr[i]
        if i != len(liststr) - 1:
            newstr += ' '
    return newstr
