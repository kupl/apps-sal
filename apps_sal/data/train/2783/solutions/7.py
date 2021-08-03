def get_grade(*arg):
    return list('FDCBAA')[max(int(sum(arg) / 30 - 5), 0)]
