def triangle(row):
    return row if len(row) == 1 else triangle("".join(process(row)))

def process(row):
    if len(row) == 1:
        yield row
    else:
        row = list(row)
        current_color = row.pop(0)
        while len(row) > 0:
            next_color = row.pop(0)
            yield color(current_color+next_color)
            current_color = next_color

def color(row):
    if len(row) == 1:
        return row
    if row in 'RR GG BB':
        return row[0]
    elif row in 'RG GR':
        return 'B'
    elif row in 'GB BG':
        return 'R'
    elif row in 'RB BR':
        return 'G'
    raise ValueError(row)
