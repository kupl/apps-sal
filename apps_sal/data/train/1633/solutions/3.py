def to_chinese_numeral(n):
    numerals = {
        "-": "负",
        ".": "点",
        0: "零",
        1: "一",
        2: "二",
        3: "三",
        4: "四",
        5: "五",
        6: "六",
        7: "七",
        8: "八",
        9: "九",
        10: "十",
        100: "百",
        1000: "千",
        10000: "万"
    }
    lst = []
    counter1 = n
    newstr = ''
    digits = '123456789'
    if counter1 == 0:
        return numerals[0]
    if counter1 < 0:
        lst.append(numerals["-"])
        counter1 *= -1
    read = str(counter1).split('.')
    if len(read[0]) == 5:
        lst.append(numerals[int(read[0][0])])
        lst.append(numerals[10000])
        if read[0][1] in digits:
            lst.append(numerals[int(read[0][1])])
            lst.append(numerals[1000])
        if read[0][1] not in digits:
            if read[0][2] in digits:
                lst.append(numerals[0])
        if read[0][2] in digits:
            lst.append(numerals[int(read[0][2])])
            lst.append(numerals[100])
        if read[0][2] not in digits:
            if read[0][3] in digits:
                lst.append(numerals[0])
        if read[0][3] in digits:
            if read[0][3] == '1':
                lst.append(numerals[1])
                lst.append(numerals[10])
            elif read[0][3] != '1':
                lst.append(numerals[int(read[0][3])])
                lst.append(numerals[10])
        if read[0][3] not in digits:
            if read[0][4] in digits:
                lst.append(numerals[0])
        if read[0][4] in digits:
            lst.append(numerals[int(read[0][4])])
    if len(read[0]) == 4:
        lst.append(numerals[int(read[0][0])])
        lst.append(numerals[1000])
        if read[0][1] in digits:
            lst.append(numerals[int(read[0][1])])
            lst.append(numerals[100])
        if read[0][1] not in digits:
            if read[0][2] in digits:
                lst.append(numerals[0])
        if read[0][2] in digits:
            if read[0][2] == '1':
                lst.append(numerals[1])
                lst.append(numerals[10])
            elif read[0][2] != '1':
                lst.append(numerals[int(read[0][2])])
                lst.append(numerals[10])
        if read[0][2] not in digits:
            if read[0][3] in digits:
                lst.append(numerals[0])
        if read[0][3] in digits:
            lst.append(numerals[int(read[0][3])])
    if len(read[0]) == 3:
        lst.append(numerals[int(read[0][0])])
        lst.append(numerals[100])
        if read[0][1] in digits:
            if read[0][1] == 1:
                lst.append(numerals[1])
                lst.append(numerals[10])
            if read[0][1] != 1:
                lst.append(numerals[int(read[0][1])])
                lst.append(numerals[10])
        if read[0][1] not in digits:
            if read[0][2] in digits:
                lst.append(numerals[0])
        if read[0][2] in digits:
            lst.append(numerals[int(read[0][2])])
    if len(read[0]) == 2:
        if read[0][0] == '1':
            lst.append(numerals[10])
        if read[0][0] != '1':
            lst.append(numerals[int(read[0][0])])
            lst.append(numerals[10])
        if read[0][1] in digits:
            lst.append(numerals[int(read[0][1])])
    if len(read[0]) == 1:
        lst.append(numerals[int(read[0])])
    if '.' in str(n):
        lst.append(numerals['.'])
        counter2 = round(n, 8)
        read2 = str(counter2).split('.')
        if len(read2[1]) == 1:
            lst.append(numerals[int(read2[1][0])])
        if len(read2[1]) == 2:
            lst.append(numerals[int(read2[1][0])])
            lst.append(numerals[int(read2[1][1])])
        if len(read2[1]) == 3:
            lst.append(numerals[int(read2[1][0])])
            lst.append(numerals[int(read2[1][1])])
            lst.append(numerals[int(read2[1][2])])
        if len(read2[1]) == 4:
            lst.append(numerals[int(read2[1][0])])
            lst.append(numerals[int(read2[1][1])])
            lst.append(numerals[int(read2[1][2])])
            lst.append(numerals[int(read2[1][3])])
        if len(read2[1]) == 5:
            lst.append(numerals[int(read2[1][0])])
            lst.append(numerals[int(read2[1][1])])
            lst.append(numerals[int(read2[1][2])])
            lst.append(numerals[int(read2[1][3])])
            lst.append(numerals[int(read2[1][4])])
        if len(read2[1]) == 6:
            lst.append(numerals[int(read2[1][0])])
            lst.append(numerals[int(read2[1][1])])
            lst.append(numerals[int(read2[1][2])])
            lst.append(numerals[int(read2[1][3])])
            lst.append(numerals[int(read2[1][4])])
            lst.append(numerals[int(read2[1][5])])
        if len(read2[1]) == 7:
            lst.append(numerals[int(read2[1][0])])
            lst.append(numerals[int(read2[1][1])])
            lst.append(numerals[int(read2[1][2])])
            lst.append(numerals[int(read2[1][3])])
            lst.append(numerals[int(read2[1][4])])
            lst.append(numerals[int(read2[1][5])])
            lst.append(numerals[int(read2[1][6])])
        if len(read2[1]) == 8:
            lst.append(numerals[int(read2[1][0])])
            lst.append(numerals[int(read2[1][1])])
            lst.append(numerals[int(read2[1][2])])
            lst.append(numerals[int(read2[1][3])])
            lst.append(numerals[int(read2[1][4])])
            lst.append(numerals[int(read2[1][5])])
            lst.append(numerals[int(read2[1][6])])
            lst.append(numerals[int(read2[1][7])])
    newstr = ''.join(lst)
    return newstr
