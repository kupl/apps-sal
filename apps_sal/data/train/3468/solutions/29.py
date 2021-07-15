from collections import  Counter
def scramble(s1, s2):
   
    dict = Counter(s1)
    dict1 = Counter(s2)

    for k in dict1.keys():
        if (not k in dict.keys()):
            return False
        if dict1[k] > dict[k]:
            return False

    return True
