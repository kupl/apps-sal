tr=str.maketrans('015','OIS')

def correct(string):
    return string.translate(tr)
