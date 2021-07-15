def reverseWords(s):
    reverse = s.split()
    strng = ""
    for i in range(1, len(reverse)+1):
        strng += reverse[-i] + " "
    return strng[:-1]
