def same_encryption(s1, s2):
    def encrypt(s): return f"{s[0]}{len(s[1:-1]) % 9}{s[-1]}"
    return encrypt(s1) == encrypt(s2)
