valid = ":) :D :-) :-D :~) :~D ;) ;D ;-) ;-D ;~) ;~D".split()


def count_smileys(arr):
    return sum(face in valid for face in arr)
