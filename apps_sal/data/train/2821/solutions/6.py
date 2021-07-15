def trim(beard):
    width = len(beard[0])
    beard = [["|" if cell in "|J" else "..." for cell in row] for row in beard[:-1]]
    beard.append(["..."] * width)
    return beard
