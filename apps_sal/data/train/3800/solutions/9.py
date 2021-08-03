from re import fullmatch, findall


def spreadsheet(s):
    if fullmatch('R\d+C\d+', s):
        row = findall('\d+', s)[0]
        col = findall('\d+', s)[1]
        return f"{convert_int(col)}{row}"
    else:
        row = findall('\d+', s)[0]
        col = findall('[A-Z]+', s)[0]
        return f"R{row}C{convert_str(col)}"


def convert_int(num, to_base=26, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n <= to_base:
        return alphabet[n]
    else:
        if n % to_base == 0:
            return convert_int(n // to_base - 1, to_base) + alphabet[26]
        else:
            return convert_int(n // to_base, to_base) + alphabet[n % to_base]


def convert_str(num):
    num = list(num)[::-1]
    answer = 0
    alphabet = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(len(num)):
        answer += alphabet.index(num[i]) * (26 ** int(i))

    return answer
