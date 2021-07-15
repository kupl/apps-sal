def format_to_list(string):
    return string.split('\n')

def stitch(array):
    return '\n'.join(array)

def vert_mirror(string):
    matrix = format_to_list(string)
    mirrored_matrix = []
    for row in matrix:
        mirrored_row = row[::-1] 
        mirrored_matrix.append(mirrored_row)
    return stitch(mirrored_matrix)

def hor_mirror(string):
    matrix = format_to_list(string)
    matrix.reverse()
    return stitch(matrix)
    
def oper(fct, s):
    return fct(s)
