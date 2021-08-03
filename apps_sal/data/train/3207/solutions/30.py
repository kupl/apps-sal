def reverseWords(s):
    s_list = s.split()
    rev_s_list = s_list[::-1]
    return " ".join(rev_s_list)
