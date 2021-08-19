def reverseWords(s):
    return ' '.join(s.split()[::-1])

    # less compact version of above:
    # s = s.split()    # create list of words
    # s = s[::-1]      # reverse the list
    # s = ' '.join(s)  # join back with spaces between
    # return s
