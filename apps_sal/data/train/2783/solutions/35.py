def get_grade(*arg):
    return list('FDCBAA')[max(int((sum(arg)/3-50)/10), 0)]
