def encrypt_once(s):
    h, t = "", ""
    for i in range(len(s)):
        if i % 2 == 0:
            h += s[i]
        else:
            t += s[i]
    return t + h


def decrypt_once(s):
    i = len(s) // 2
    j = 0
    
    result = ""
    
    for k in range(len(s)):
        if k % 2 == 0:
            result += s[i]
            i += 1
        else:
            result += s[j]
            j += 1
    
    return result


def decrypt(text, n):
    if not text or len(text) == 0 or n <= 0:
        return text

    for i in range(n):
        text = decrypt_once(text)

    return text


def encrypt(text, n):
    if not text or len(text) == 0 or n <= 0:
        return text
        
    for i in range(n):
        text = encrypt_once(text)
    
    return text

