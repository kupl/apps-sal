def words_to_object(s):
    s = s.split()
    return "[" + ', '.join(["{name : '%s', id : '%s'}"%(i,j) for i,j in zip(s[::2], s[1::2])]) + "]"
