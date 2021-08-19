def scramble(s1, s2):
    counter01 = [0] * 26
    counter02 = [0] * 26
    for char in s1:
        counter01[ord(char) - 97] += 1
    for char in s2:
        counter02[ord(char) - 97] += 1
    for i in range(26):
        if counter01[i] < counter02[i]:
            return False
    return True
