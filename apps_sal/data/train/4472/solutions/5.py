def bear_fur(bears):
    if bears[0] == bears[1]:
        return bears[0]
    if 'black' in bears and 'white' in bears:
        return 'grey'
    if 'black' in bears and 'brown' in bears:
        return 'dark brown'
    if 'white' in bears and 'brown' in bears:
        return 'light brown'
    return 'unknown'
