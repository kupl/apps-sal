def words_to_marks(s):
    sum = 0
    for ch in s:
        sum+=(ord(ch)-96)
    #end for
    return sum
