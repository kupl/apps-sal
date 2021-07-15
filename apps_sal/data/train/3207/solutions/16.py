def reverseWords(str):
    a = str.split(" ")
    b = ""
    c = a[::-1]
    for i in range(0,len(a)):
        if i != len(a)-1:
            b += c[i] + " "
        else:
            b +=c[i]
    return(b)
