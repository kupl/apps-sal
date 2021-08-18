def generate_hashtag(s):
    if len(s) == 0 or len(s) >= 140:
        return False
    a = s.split()
    st = ''
    for i in range(len(a)):
        st += str(a[i].capitalize())
    return '
