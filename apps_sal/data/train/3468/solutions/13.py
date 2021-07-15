def scramble(s1, s2):
        return not False in([s1.count(i)>=s2.count(i) for i in set(s2)])

#set() <3

