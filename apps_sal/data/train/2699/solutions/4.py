def number2words(n):
    if n == 0:
        return "zero"
    if n == 10:
        return "ten"

    numbers_11_19 = {
        "0": "ten",
        "1": "eleven",
        "2": "twelve",
        "3": "thirteen",
        "4": "fourteen",
        "5": "fifteen",
        "6": "sixteen",
        "7": "seventeen",
        "8": "eighteen",
        "9": "nineteen"
    }
    numbers_1_9 = {
        "0": "",
        '1': 'one',
        '2': 'two',
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
    }
    numbers_20_100 = {
        "0": "",
        "2": "twenty",
        "3": "thirty",
        "4": "forty",
        "5": "fifty",
        "6": "sixty",
        "7": "seventy",
        "8": "eighty",
        "9": "ninety",
    }

    nStr = str(n)
    print(nStr)
    s = ""
    L = len(nStr)
    pos = 0
    if pos == L - 6:
        s += numbers_1_9.get(nStr[pos])
        if nStr[pos] != "0":
            s += " hundred "
        pos += 1
    if pos == L - 5:
        if nStr[pos] == "1":
            s += numbers_11_19.get(nStr[pos + 1])
            pos = +1
        else:
            s += numbers_20_100.get(nStr[pos])
            if nStr[pos + 1] != "0" and nStr[pos] != "0":
                s += "-"
        pos += 1
    if pos == L - 4:
        if nStr[pos - 1] != "1":
            s += numbers_1_9.get(nStr[pos])
        s += " thousand "
        pos += 1
    if pos == L - 3:
        s += numbers_1_9.get(nStr[pos])
        if nStr[pos] != "0":
            s += " hundred "
        pos += 1
    if pos == L - 2:
        if nStr[pos] == "1":
            s += numbers_11_19.get(nStr[pos + 1])
            pos = -1
        else:
            s += numbers_20_100.get(nStr[pos])
            if nStr[pos + 1] != "0" and nStr[pos] != "0":
                s += "-"
        pos += 1
    if pos == L - 1:
        s += numbers_1_9.get(nStr[pos])
    return s.strip()
