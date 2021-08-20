def consonant_count(s):
    return sum((1 for x in s if 'b' <= x.lower() <= 'z' and x not in 'eiou'))
