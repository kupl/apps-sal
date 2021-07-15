def add(s1, s2):
    count = 0
    for i in range(len(s1)+len(s2)):
        if i < len(s1):
            count += ord(s1[i])
        if i< len(s2):
            count += ord(s2[i])
    return count

