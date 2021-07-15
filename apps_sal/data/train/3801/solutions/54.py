import string
def words_to_marks(s):
    alpha={}
    j=1
    for i in string.ascii_lowercase:
        alpha[i]=j
        j=j+1
    j=0
    for a in s:
        j=j+alpha[a]
    return j
