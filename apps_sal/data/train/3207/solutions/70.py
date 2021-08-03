def reverseWords(s):
    s = s.split(" ")
    s.reverse()

    res = " ".join(s)

    return res
