def compare(s1, s2):
    if s1 == None or not s1.isalpha():
        s1 = ""
    if s2 == None or not s2.isalpha():
        s2 = ""

    sum_1 = 0
    for char in s1:
        sum_1 += ord(char.upper())

    sum_2 = 0
    for char in s2:
        sum_2 += ord(char.upper())

    return sum_1 - sum_2 == 0
