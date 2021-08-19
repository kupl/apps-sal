def calculate_ratio(w, h):
    for i in range(1, 100000):
        if w == 0:
            return 'You threw an error'
        elif w / h * i - int(w / h * i) == 0:
            return str(int(w / h * i)) + ':' + str(i)
        elif h / w * i - int(h / w * i) == 0:
            return str(i) + ':' + str(int(h / w * i))
    return 'You threw an error'
