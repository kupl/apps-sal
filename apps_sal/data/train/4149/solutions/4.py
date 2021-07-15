from string import ascii_lowercase as lowers, digits


rotlow = f"{lowers[13:]}{lowers[:13]}"
rotdig = f"{digits[5:]}{digits[:5]}"
table = str.maketrans(
    f"{lowers}{lowers.upper()}{digits}",
    f"{rotlow}{rotlow.upper()}{rotdig}",
)


def ROT135(input):
    return input.translate(table)
