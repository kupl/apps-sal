def scramble(s1, s2):
    """ returns true of a porton of s1 can be rearranged to match s2. Basic concept: use an indicator 
    dictionary  of the counts of letters in s2, check if s1 has sufficient occurences of each letter to make
    that indicator == 0 for all chars"""
    
    cts = [s2.count(i) for i in list(set(s2)) ] # count occurence of letters
    dic = dict(zip(list(set(s2)) ,cts)) # dictionary of counts.
    truth = True
    
    for char in list(s1):
        try:
            if dic[char] > 0: # If dic[char] already == 0, we know there are suff. occurrences of that char
                dic[char] = (dic[char] - 1) 
        except KeyError:
            pass
    
    if sum(dic.values()) > 0: # if all chars sufficiently occur, sum should be 0
        truth = False

    return truth
