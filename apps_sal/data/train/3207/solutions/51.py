def reverseWords(s):
    a = "".join(i + " " for i in s.split()[::-1])
    return a[:-1]
