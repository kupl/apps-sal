def reverseWords(s):
    reverse_s = s.split()
    reverse_s.reverse()
    s = " ".join(reverse_s)
    return s
