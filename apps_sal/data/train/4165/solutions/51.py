def uni_total(string):
    toplam = 0
    for i in string:
        toplam += int(str(ord(i)))
    return toplam
