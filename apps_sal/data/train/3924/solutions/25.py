def reverse_words(text):

    return ' '.join((text[::-1]).split(' ')[::-1])
    
    """
    rev=text[::-1]
    lst_rev=rev.split(' ')
    lst=lst_rev[::-1]
    str=' '.join(lst)
    return str
    """
