import re

MORSE_TO_INT = {
    ".----": "1", "..---": "2", "...--": "3",
    "....-": "4", ".....": "5", "-....": "6",
    "--...": "7", "---..": "8", "----.": "9",
    "-----": "0"
}


def morse_converter(string):
    return int("".join(MORSE_TO_INT[x] for x in re.findall(".....", string)))
