from collections import Counter as count
def scramble(s1,s2):
    return len(count(s2)- count(s1)) == 0
