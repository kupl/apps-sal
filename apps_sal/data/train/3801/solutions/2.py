def words_to_marks(s):
    return sum( ord(i)-(ord('a')-1) for i in s )
