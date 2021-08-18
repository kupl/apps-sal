conv = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
    "thousand": 1000,
    "million": 1000000
}


def parse99(s: str):
    num = 0
    for wd in s.split("-"):
        num += conv.get(wd.strip(), 0)
    return num


def parseHundreds(s: str):
    s = s.split("hundred")
    if len(s) == 1:
        return parse99(s[0])
    else:
        return parse99(s[0]) * 100 + parse99(s[1])


def parseThousands(s: str):
    s = s.split("thousand")
    if len(s) == 1:
        return parseHundreds(s[0])
    else:
        return parseHundreds(s[0]) * 1000 + parseHundreds(s[1])


def parseMillions(s: str):
    s = s.split("million")
    if len(s) == 1:
        return parseThousands(s[0])
    else:
        return parseThousands(s[0]) * 1000000 + parseThousands(s[1])


def parse_int(s: str):
    return parseMillions(s.replace(" and ", " "))
