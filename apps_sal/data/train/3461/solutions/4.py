def common_ground(s1,s2):
    ret = [i for i in set(s1.split()) if i in s2.split()]
    if len(ret) == 0: return 'death'
    return ' '. join(sorted(ret, key=lambda x: (s2.split()).index(x) ))
