def to_leet_speak(str):
    (newStr, replace) = ('', '@8(D3F6#!JK1MN0PQR$7UVWXY2')
    for each in str:
        if ord(each) - ord('A') >= 0 <= 26:
            newStr += replace[ord(each) - ord('A')]
        else:
            newStr += each
    return newStr
