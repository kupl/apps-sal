def words_to_marks(s):
    alf = ' abcdefghijklmnopqrstuvwxyz'
    sum_out = 0
    for q in range(len(s)):
        sum_out = sum_out + alf.find(s[q])
    return sum_out
