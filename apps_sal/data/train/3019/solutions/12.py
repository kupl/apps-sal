def str_count(strng, letter):
    from collections import Counter
    temp = Counter(strng)
    try:
        return temp[letter]
    except:
        return 0
