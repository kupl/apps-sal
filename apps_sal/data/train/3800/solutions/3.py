import re


def spreadsheet(s):
    numbers = re.findall(r"(\d+)", s)
    if len(numbers) == 1:
        row = numbers[0]
        col = sum(26**i * (ord(v) - 64) for i, v in enumerate(s[:s.find(row)][::-1]))
        return "R{row}C{col}".format(row=row, col=col)
    else:
        row = numbers[0]
        x = int(numbers[1])
        col = ""
        while x > 0:
            col = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(x - 1) % 26] + col
            x = (x - 1) // 26
        return "{col}{row}".format(col=col, row=row)
