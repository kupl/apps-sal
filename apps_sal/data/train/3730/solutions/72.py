def capitalize(s):
  # given a string
    # capitalize the letters in the even positions
    # capitalize those that are in odd positions separately
    #0 is even
    # given a string of letters
    #     when a letter occupy the even indexes
    #     then capitalise
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
