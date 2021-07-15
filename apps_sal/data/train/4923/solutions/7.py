from collections import Counter

def count_feelings(s, arr):
    count = sum([1 for word in arr if len(Counter(word) - Counter(s))==0])
    return "{} feeling{}.".format(count,"" if count==1 else "s")
