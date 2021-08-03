def lowercase_count(strng):
    total = 0
    for i in list(strng):
        if i in list('qwertyuiopasdfghjklzxcvbnm'):
            total = total + 1
    return total
