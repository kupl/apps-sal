a = ord('a')
A = ord('A')
z = ord('z')
Z = ord('Z')
upperToLower = A - a
lowerToUpper = a - A


def alternateCase(s):
    str = ""
    for i in range(len(s)):
        if ord(s[i]) >= A and ord(s[i]) <= Z:
            # convert to lower case
            str += chr(ord(s[i]) - upperToLower)
        elif ord(s[i]) >= a and ord(s[i]) <= z:
            # convert to upper case
            str += chr(ord(s[i]) - lowerToUpper)
        else:
            str += s[i]
    return str
