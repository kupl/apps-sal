import string


def contamination(text, char):
    if not text or not char:
        return ''
    intab = string.printable
    outtab = char * len(intab)
    transtab = str.maketrans(intab, outtab)
    return text.translate(transtab)
