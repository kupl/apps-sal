def str_count(stroka, letter):
    spisok = list(stroka)
    razi = 0
    x = 0
    while x != len(spisok):
        if spisok[x] == letter:
            razi = razi + 1
            x = x + 1
        else:
            x = x + 1
    return razi
