def triangle(row):
    buffer = ''
    
    while len(row) > 1:
        aux_string = ''
        
        for i, char in enumerate(row):
            if i + 1 < len(row):
                buffer = char + row[i+1]
                if char == row[i+1]:
                    aux_string += char
                elif not 'R' in buffer:
                    aux_string += 'R'
                elif not 'G' in buffer:
                    aux_string += 'G'
                elif not 'B' in buffer:
                    aux_string += 'B'
        
        row = aux_string
    return row
