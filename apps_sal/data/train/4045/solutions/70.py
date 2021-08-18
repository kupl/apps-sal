def number(lines):
    new_lines = []
    cadena = ''
    if lines != []:

        for i in range(len(lines)):
            cadena = str(i + 1) + ':' + ' ' + lines[i]
            new_lines.append(cadena)
        return new_lines
    else:
        return lines
