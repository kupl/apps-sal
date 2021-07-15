def build_palindrome(str):
    suf = ""
    for c in str:
        pal = str + suf
        if pal == pal[::-1]:
            return pal
        suf = c + suf
