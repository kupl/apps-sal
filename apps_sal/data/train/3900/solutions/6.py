def segment_display(num):
    fline, fl, fr, frl, empty = ['
    codes= [
        empty * 9,
        fline + frl * 3 + empty + frl * 3 + fline,
        (empty + fr * 3) * 2 + empty,
        fline + fr * 3 + fline + fl * 3 + fline,
        (fline + fr * 3) * 2 + fline,
        empty + frl * 3 + fline + fr * 3 + empty,
        fline + fl * 3 + fline + fr * 3 + fline,
        fline + fl * 3 + fline + frl * 3 + fline,
        fline + (fr * 3 + empty) * 3 + empty,
        (fline + frl * 3) * 2 + fline,
        fline + frl * 3 + fline + fr * 3 + fline
    ]

    result= ""
    for line in range(9):
        result += "|" + "|".join([codes[0 if letter == ' ' else int(letter) + 1][line] for letter in str(num).rjust(6)]) + "|\n"
    return result[:-1]
