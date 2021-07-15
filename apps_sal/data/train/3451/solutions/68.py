def triangle(row):
    
    if len(row) == 1:
        return row
    
    while len(row) > 1:
        N = len(row)
        new_row = []
        i = 0
        while i < N-1:
            
            word = [row[i], row[i+1]]
            word.sort()
            word = ''.join(word)
            if word =='BG':
                new_row.append('R')
            elif word == 'GR':
                new_row.append('B')
            elif word == 'BR':
                new_row.append('G')
            elif word == 'GG':
                new_row.append('G')
            elif word == 'RR':
                new_row.append('R')            
            elif word == 'BB':
                new_row.append('B')
            else:
                return False
            
            i += 1
            
        row = new_row
    return row[0]
