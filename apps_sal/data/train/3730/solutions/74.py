def capitalize(s):
    # BDD
    # Given a sring
    # When capitalize letters with even indexes

    # ps
    # 3lists
    # for loop thet will loop through the string
    # If statement
    even = []
    odd = []
    final = []
    for i in range(len(s)):
        if i % 2 == 0:
            a = s[i].capitalize()
            even.append(a)
        else:
            even.append(s[i])
    for i in range(len(s)):
        if i % 2 != 0:
            b = s[i].capitalize()
            odd.append(b)
        else:
            odd.append(s[i])
    finaleven = ''.join(even)
    finalodd = ''.join(odd)
    final.append(finaleven)
    final.append(finalodd)
    return final
