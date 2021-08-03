table = {char: str(i + 10 * j + 11)
         for j, row in enumerate("ABCDE FGHIK LMNOP QRSTU VWXYZ".split())
         for i, char in enumerate(row)}


def polybius(text):
    return "".join(table.get(char, " ") for char in text.replace("J", "I"))
