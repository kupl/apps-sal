def string_to_array(s):
    if len(s) > 1:  # if string has characters
        return s.split()  # split string into pieces
    else:
        return ['']
