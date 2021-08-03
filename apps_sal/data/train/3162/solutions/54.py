def compare(s1, s2):
    s1_list = []
    s2_list = []

    if s1 != None:
        for i in s1:
            if i.isalpha():
                s1_list.append(ord(i.upper()))
            else:
                s1_list = []
    else:
        s2_list = []

    if s2 != None:
        for i in s2:
            if i.isalpha():
                s2_list.append(ord(i.upper()))
            else:
                s2_list = []
    else:
        s2_list = []

    return sum(s1_list) == sum(s2_list)
