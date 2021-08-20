def elapsed_seconds(s, e):
    ls = str(e - s).split(':')
    return int(ls[0]) * 3600 + int(ls[1]) * 60 + int(ls[2])
