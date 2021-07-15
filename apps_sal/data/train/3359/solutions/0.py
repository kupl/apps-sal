def title_to_number(title):
    ret = 0
    for i in title:
        ret = ret*26 + ord(i) - 64
    return ret
