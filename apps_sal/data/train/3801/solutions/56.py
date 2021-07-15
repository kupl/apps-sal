alpha="-abcdefghijklmnopqrstuvwxyz"
def words_to_marks(s):
    return sum ( [alpha.index(x)  for x in s] )
