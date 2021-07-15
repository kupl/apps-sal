def words_to_marks(s):
    l='abcdefghijklmnopqrstuvwxyz'
    res=0
    for i in s:
        res+=l.index(i)+1
    return res
