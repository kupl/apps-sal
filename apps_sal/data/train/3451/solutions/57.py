def triangle(row):
    translate = {"GG": "G", "RR": "R", "BB": "B", "BG": "R", "RG":"B", "BR":"G", "GB": "R", "GR":"B", "RB":"G"}
    while len(row) > 1:
        row = ''.join(translate[row[i:i+2]] for i in range(len(row)-1))
    return row
