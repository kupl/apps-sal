import string
def words_to_marks(s):
    # Easy one
    letters = string.ascii_lowercase
    total = 0
    
    for i in s:
        total += letters.index(i) + 1

    return total
    

