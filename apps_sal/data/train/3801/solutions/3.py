def words_to_marks(s):
    return sum(map(ord,s))-len(s)*96
