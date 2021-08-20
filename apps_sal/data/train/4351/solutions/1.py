def find_middle(string):
    if string is None:
        return -1
    if type(string) is int:
        return -1
    if type(string) is list:
        return -1
    spisok = []
    for i in string:
        if i.isdigit():
            spisok.append(i)
    if len(spisok) == 0:
        return -1
    spisok_ans = 1
    for i in spisok:
        spisok_ans *= int(i)
    spisok = str(spisok_ans)
    if len(spisok) % 2 == 0:
        if len(spisok) >= 2:
            spisok[:1].replace('0', '')
        test = int(len(spisok) / 2)
        answer = spisok[test - 1:test + 1]
    else:
        test = int(len(spisok) / 2)
        answer = spisok[test:test + 1]
    answer = ''.join(answer)
    return int(answer)
