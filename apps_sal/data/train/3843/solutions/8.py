import string

region = string.ascii_uppercase + string.ascii_lowercase + ''.join(str(x) for x in range(10)) + ".,:;-?! '()$%&\""


def switch_case(char):
    return char.lower() if char.isupper() else char.upper() if char.islower() else char


def decrypt(encrypted_text):
    if (encrypted_text is None) or (encrypted_text == ''):
        return encrypted_text
    current_char = region[-region.index(encrypted_text[0]) - 1]
    ret = current_char
    for char in list(encrypted_text)[1:]:
        ret += region[(region.index(ret[-1]) - region.index(char)) % 77]
    ret = ''.join([switch_case(x) if i % 2 != 0 else x for i, x in enumerate(ret)])
    return ret


def encrypt(text):
    if (text is None) or (text == ''):
        return text
    text = ''.join([switch_case(x) if i % 2 != 0 else x for i, x in enumerate(text)])
    index_char, index_next = [region.index(char) for char in text], [region.index(char) for char in text[1:]]
    text = region[-region.index(text[0]) - 1] + ''.join([region[(c - n) % 77] for c, n in zip(index_char, index_next)])
    return text
